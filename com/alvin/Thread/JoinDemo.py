# encoding: utf-8
import threading
import time


class MyThread(threading.Thread):
    def __init__(self, threadName):
        threading.Thread.__init__(self, name=threadName)

    def run(self):
        print(self.getName())

if __name__ == '__main__':
    t1 = MyThread('t1')
    t1.run()
    t1.setName('t1')
    t1.run()
    t2 = MyThread('t2')
    t2.start()