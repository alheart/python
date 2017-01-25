import threading

def func():
	print('func() passed to thread')

t = threading.Thread(target=func)
t.start()


class MyThread(threading.Thread):
	def run(self):
		print('MyThread extended from thread')
		pass

t = MyThread()
t.start()