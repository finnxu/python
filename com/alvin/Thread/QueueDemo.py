# encoding: utf-8
import threading
import queue


class produce(threading.Thread):
    def __init__(self, threadname):
        threading.Thread.__init__(self, name=threadname)

    def run(self):
        global que
        que.put(self.getName())
        print(self.getName(), 'put', self.getName(), 'to queue')


class comsumer(threading.Thread):
    def __init__(self, threadname):
        threading.Thread.__init__(self, name=threadname)

    def run(self):
        global que
        que.put(self.getName())
        print(self.getName(), 'put', self.getName(), 'to queue')


if __name__ == '__main__':
    que = queue.Queue()
    pList = []
    cList = []
    for i in range(10):
        p = produce('produce:')
        pList.append(p)
    for i in range(10):
        c = comsumer('comsumer:')
        cList.append(c)
    for i in pList:
        i.start()
        i.join()
    for i in cList:
        i.start()
        i.join()
