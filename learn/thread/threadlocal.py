import threading

local = threading.local()
local.tname = 'main'

def func():
	local.tname = 'notmain'
	print(local.tname)
	pass

t1 = threading.Thread(target=func)


t1.start()
t1.join()


print(local.tname)