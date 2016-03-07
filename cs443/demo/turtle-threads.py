# turtle-threads.py
import threading
import time
import random

DATA = 0

class ThreadA(threading.Thread):
    def __init__(self, e):
        threading.Thread.__init__(self)
        self.runtime = e
        
    def run(self):
        while self.runtime.is_set():
            # time.sleep(2)
            threadLock.acquire()
            writer()
            # time.sleep()
            threadLock.release()


class ThreadB(threading.Thread):
    def __init__(self, e):
        threading.Thread.__init__(self)
        self.runtime = e

    def run(self):
        while self.runtime.is_set():
            # time.sleep(1)
            threadLock.acquire()
            reader()
            # time.sleep()
            threadLock.release()

def writer():
    global DATA
    DATA = DATA + 1
    print 'WRITE=>', DATA
    
def reader():
    global DATA
    DATA = DATA - 1
    print 'READ==>', DATA


threadLock = threading.Lock()
runtime_e = threading.Event()
runtime_e.set()

ta = ThreadA(runtime_e)
tb = ThreadB(runtime_e)


ta.start()
tb.start()

try:
    while True:
        time.sleep(0.5)

except KeyboardInterrupt:
    runtime_e.clear()








