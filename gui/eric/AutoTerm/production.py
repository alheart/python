import sys,  time, threading

class Production:
    def __init__(self, miniterm, msg, process):
        self.miniterm = miniterm
        self.msg = msg
        self.process = process
        
    def start(self):
        self.alive = True
        # start serial->console thread
        self.work_thread = threading.Thread(target=self.work)
        self.work_thread.setDaemon(1)
        self.work_thread.start()
        
    def work(self):
        self.uboot_to_prompt()
        self.process(10)
        self.set_env()
        self.process(20)
        self.write_kernel()
        self.process(30)
    
    def uboot_to_prompt(self):
        self.miniterm.screen_clr()
        sys.stderr.write("\nPlease reset DUT\n")
        self.msg("Please power ON DUT", color='green')
        #miniterm.write("\n\n\n\n\n\n")
        while not self.miniterm.screen_wait_for("Hit any key to stop autoboot:", 5, True):
            sys.stderr.write("\nPlease press DUT reset button\n")
            self.msg("Power ON Reset FAIL! Press DUT reset button", color='red')
            #miniterm.write("\n")
    
        self.miniterm.write("\n")
        #sys.stderr.write("\nentering U-Boot\n")
        time.sleep(0.3)
        self.msg("Press DUT Reset button", color='green')
        while self.miniterm.screen_find("hisilicon # ", True) == 0:
            self.miniterm.write("\n")
            
    def set_env(self):
        self.uboot_setenv("ipaddr", "169.254.1.177")
        self.uboot_setenv("netmask", "255.255.0.0")
        self.uboot_setenv("serverip", "169.254.1.156")

    def uboot_setenv(self, name, value):
        self.miniterm.screen_clr()
        self.msg("Set %s to %s" % (name, value))
        self.miniterm.write("setenv %s %s" % (name, value))
    
        if not self.miniterm.screen_wait_for("setenv %s %s" % (name, value), 3, True):
            raise UserWarning("setenv %s to %s fail?!" % (name, value), None)
    
        self.miniterm.write("\n")
        if not self.miniterm.screen_wait_for("hisilicon #", 3, True):
            raise UserWarning("setenv %s to %s fail?!!" % (name, value), None)

    def write_to_serial(self, msg, timeout=3):
        self.miniterm.write(msg)
        self.msg(msg)
        if not self.miniterm.screen_wait_for("%s" % msg, timeout, True):
            raise UserWarning("%s fail?!" % msg, None)
        
        self.miniterm.write("\n")
        if not self.miniterm.screen_wait_for("hisilicon #", timeout, True):
            self.msg("%s fail?!!" % msg, level='error')
            raise UserWarning("%s fail?!!" % msg, None)

    def write_kernel(self):
        self.miniterm.screen_clr()
        self.write_to_serial("mw.b 82000000 ff f00000")
        
        self.write_to_serial("tftp 82000000 IPS3000_kernel_v1.1.0.image", timeout=10)
        self.msg("Dowload kenerl success!", level='success')
        self.write_to_serial("nand erase 100000 f00000", timeout=10)
        self.write_to_serial("nand write 82000000 100000 f00000", timeout=10)
        
    def write_rootfs(self):
        self.miniterm.screen_clr()
        self.write_to_serial("mw.b 82000000 ff 2000000")
        
        self.write_to_serial("tftp 82000000 IPS3000_rootfs_v1.2.4.C50.yaffs2", timeout=10)
        self.msg("Dowload rootfs success!", level='success')
        self.write_to_serial("nand erase 1000000 F000000")
        self.write_to_serial("nand write.yaffs 82000000 1000000 ")
