import threading

'''
    使用event实现线程间通信
'''


class mythread(threading.Thread):
    def __init__(self, threadname):
        threading.Thread.__init__(self, name=threadname)

    def run(self):
        global event
        if event.isSet():
            event.clear()
            event.wait()
            print('event is set', self.getName())
        else:
            print('event is not set', self.getName())
            event.set()


event = threading.Event()
event.set()
t1 = []
for i in range(10):
    t = mythread(str(i))
    t1.append(t)
for i in t1:
    i.start()
