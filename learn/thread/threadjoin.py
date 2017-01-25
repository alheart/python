import threading
import time

def context(tJoin):
	print('in threadContext.')
	tJoin.start()

	tJoin.join()

	print('out threadContext.')
	pass

def join():
	print('in threadJoin.')
	time.sleep(5)

	print('out threadJoin.')
	pass

tJoin = threading.Thread(target=join)
tContext = threading.Thread(target=context, args=(tJoin,))

tContext.start()
