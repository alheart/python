import threading
import time

product = None
con = threading.Condition()

def produce():
	global product

	if con.acquire():
		while True:
			if product is None:
				print('Produce..', sep=" ")
				product = 'anything'
				con.notify()

			con.wait()
			time.sleep(2)
	pass

def consume():
	global product

	if con.acquire():
		while True:
			if product is not None:
				print('consume...')
				product = None
				con.notify()

			con.wait()
			#time.sleep(2)
			pass
	pass

t1 = threading.Thread(target=produce)
t2 = threading.Thread(target=consume)

t2.start()
t1.start()