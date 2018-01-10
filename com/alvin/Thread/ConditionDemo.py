# encoding: utf-8
import threading

'''
    生产者消费者问题(多线程模拟实现)
'''


class Produce(threading.Thread):
    def __init__(self, threadname):
        threading.Thread.__init__(self, name=threadname)

    def run(self):
        global x
        con.acquire()
        if x == 100:
            con.wait()
            pass
        else:
            for i in range(100):
                x = x + 1
                print('produce :', x)
            con.notify()
        print('produce :', x)
        con.release()


class Comsumer(threading.Thread):
    def __init__(self, threadname):
        threading.Thread.__init__(self, name=threadname)

    def run(self):
        global x
        con.acquire()
        if x == 0:
            con.wait()
            pass
        else:
            for i in range(100):
                x = x - 1
                print('comsumer :', x)
            con.notify()
        print('comsumer :', x)
        con.release()


if __name__ == '__main__':
    con = threading.Condition()
    x = 0
    p = Produce('produce:')
    c = Comsumer('comsumer:')
    p.start()
    c.start()
    p.join()
    c.join()
    print('x :', x)
