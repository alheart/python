import sys, serial, threading, time

CONVERT_CRLF = 2
CONVERT_CR   = 1
CONVERT_LF   = 0
NEWLINE_CONVERISON_MAP = ('\n', '\r', '\r\n')
LF_MODES = ('LF', 'CR', 'CR/LF')

REPR_MODES = ('raw', 'some control', 'all control', 'hex')

class Miniterm:
    def __init__(self, port, baudrate, parity, rtscts, xonxoff, echo=False, convert_outgoing=CONVERT_CRLF, repr_mode=0):
        try:
            self.serial = serial.serial_for_url(port, baudrate, parity=parity, rtscts=rtscts, xonxoff=xonxoff)
        except AttributeError:
            # happens when the installed pyserial is older than 2.5. use the
            # Serial class directly then.
            self.serial = serial.Serial(port, baudrate, parity=parity, rtscts=rtscts, xonxoff=xonxoff)
        self.echo = echo
        self.repr_mode = repr_mode
        self.convert_outgoing = convert_outgoing
        self.newline = NEWLINE_CONVERISON_MAP[self.convert_outgoing]
        self.dtr_state = True
        self.rts_state = True
        self.break_state = False

    def start(self):
        self.alive = True
        # start serial->console thread
        self.receiver_thread = threading.Thread(target=self.reader)
        self.receiver_thread.setDaemon(1)
        self.receiver_thread.start()
        # enter console->serial loop

    def stop(self):
        self.alive = False

    def join(self, transmit_only=False):
        self.transmitter_thread.join()
        if not transmit_only:
            self.receiver_thread.join()

    def dump_port_settings(self):
        sys.stderr.write("\n--- Settings: %s  %s,%s,%s,%s\n" % (
            self.serial.portstr,
            self.serial.baudrate,
            self.serial.bytesize,
            self.serial.parity,
            self.serial.stopbits,
        ))
        sys.stderr.write('--- RTS %s\n' % (self.rts_state and 'active' or 'inactive'))
        sys.stderr.write('--- DTR %s\n' % (self.dtr_state and 'active' or 'inactive'))
        sys.stderr.write('--- BREAK %s\n' % (self.break_state and 'active' or 'inactive'))
        sys.stderr.write('--- software flow control %s\n' % (self.serial.xonxoff and 'active' or 'inactive'))
        sys.stderr.write('--- hardware flow control %s\n' % (self.serial.rtscts and 'active' or 'inactive'))
        sys.stderr.write('--- data escaping: %s\n' % (REPR_MODES[self.repr_mode],))
        sys.stderr.write('--- linefeed: %s\n' % (LF_MODES[self.convert_outgoing],))
        try:
            sys.stderr.write('--- CTS: %s  DSR: %s  RI: %s  CD: %s\n' % (
                (self.serial.getCTS() and 'active' or 'inactive'),
                (self.serial.getDSR() and 'active' or 'inactive'),
                (self.serial.getRI() and 'active' or 'inactive'),
                (self.serial.getCD() and 'active' or 'inactive'),
                ))
        except serial.SerialException:
            # on RFC 2217 ports it can happen to no modem state notification was
            # yet received. ignore this error.
            pass

    def reader(self):
        """loop and copy serial->console"""
        try:
            while self.alive:
                data = self.serial.read()
                datastr=data.decode()
                #sys.stdout.write(datastr)
                self.screen = self.screen + datastr

                if self.repr_mode == 0:
                    # direct output, just have to care about newline setting
                    if datastr == '\r' and self.convert_outgoing == CONVERT_CR:
                        sys.stdout.write('\n')
                    else:
                        sys.stdout.write(datastr)
                elif self.repr_mode == 1:
                    # escape non-sys.stdout.writeable, let pass newlines
                    if self.convert_outgoing == CONVERT_CRLF and datastr in '\r\n':
                        if datastr == '\n':
                            sys.stdout.write('\n')
                        elif datastr == '\r':
                            pass
                    elif datastr == '\n' and self.convert_outgoing == CONVERT_LF:
                        sys.stdout.write('\n')
                    elif datastr == '\r' and self.convert_outgoing == CONVERT_CR:
                        sys.stdout.write('\n')
                    else:
                        sys.stdout.write(repr(datastr)[1:-1])
                elif self.repr_mode == 2:
                    # escape all non-sys.stdout.writeable, including newline
                    sys.stdout.write(repr(datastr)[1:-1])
                elif self.repr_mode == 3:
                    # escape everything (hexdump)
                    for character in datastr:
                        sys.stdout.write("%s " % character.encode('hex'))
                sys.stdout.flush()
        except serial.SerialException as e:
            self.alive = False
            # would be nice if the console reader could be interruptted at this
            # point...
            raise

    def screen_clr(self):
        self.screen = ''

    def screen_find(self, match_str, clear=False):
        """Try to find the match_str in screen buffer.
           Return counts of matches or 0 if not found.
           It is a blocking call.
        """
        found = self.screen.count(match_str)
        if found != 0 and clear:
            self.screen = self.screen.partition(match_str)[2]
        return found

    def screen_find_list(self, match_str_list, clear=False):
        """Try to find the match_str(in match_str_list) in screen buffer.
           Return counts of matches or 0 if not found.
           It is a blocking call.
        """
        found = 0
        for ms in match_str_list:
            sys.stderr.write("M(%s)" % ms)
            found = self.screen.count(ms)
            if found != 0:
                break

        if clear:
            self.screen = ''
        return found

    def screen_find_old(self, match_str, clear=False):
        """Try to find the match_str in screen buffer.
           Return found_idx if found, otherwise return -1.
           It is non-blocking call.
        """
        found = False
        found_idx = -1
        idx = self.screen.find(match_str)
        while idx != -1:
            found = True
            found_idx = idx
            idx = self.screen.find(match_str, idx)

        if found:
            if clear:
                self.screen = self.screen[found_idx:]
            return found_idx
        else:
            return -1

    def screen_wait_for(self, match_str, timeout=-1, clear=False):
        s = 0
        found = self.screen_find(match_str, clear)
        while found == 0:
            if timeout != -1 and s > timeout:
                break
            time.sleep(0.1)
            s = s + 0.1
            found = self.screen_find(match_str, clear)

        if found != 0:
            #sys.stderr.write("Found!!")
            return True
        else:
            #sys.stderr.write("Not found!")
            return False


    def write(self, str):
        for c in str[:]:
            if c == '\n':
                self.serial.write(self.newline.encode('utf-8'))         # send newline character(s)
                if self.echo:
                    sys.stdout.write(c.encode('utf-8'))                 # local echo is a real newline in any case
                    sys.stdout.flush()
            else:
                self.serial.write(c.encode('utf-8'))                    # send character
                if self.echo:
                    sys.stdout.write(c.encode('utf-8'))
                    sys.stdout.flush()
            self.serial.flush()
            time.sleep(0.01)

    def is_alive(self):
        return self.alive
