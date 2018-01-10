# encoding: utf-8
import threading

'''
    多线程编程
'''


class myThread(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self):
        print('i am', self.num)


def run(x, y):
    for i in range(x, y):
        t1 = threading.Thread(target=run, args=(10, 20))
        t1.start()
        t2 = threading.Thread(target=run, args=(20, 50))
        t2.start()


if __name__ == '__main__':
    t1 = myThread(1)
    t2 = myThread(2)
    t3 = myThread(3)

    t1.start()
    t2.start()
    t3.start()

    print('threading-----------2----')
