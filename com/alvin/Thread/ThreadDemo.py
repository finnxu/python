# encoding: utf-8
import _thread
def run(n):
    for i in range(n):
        print (i)
if __name__ == '__main__':
    _thread.start_new_thread(run(4))