#!/usr/bin/python

import threading
import time
import random

COUNT = 2

class producerThread(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):
        print "Starting " + self.name 
        while True:
            time.sleep(random.randint(1,5))
            threadLock.acquire() 
            mod_count(random.randint(2,3))
            threadLock.release()     

class consumerThread(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):
        print "Starting " + self.name
        while True: 
            threadLock.acquire() 
            read_count()
            threadLock.release()

def mod_count(scale):
    global COUNT
    COUNT = COUNT * scale


def read_count():
    global COUNT
    print 'COUNT==>', COUNT


""" SETUP """

threadLock = threading.Lock()
threads = []

# Create new threads
producer = producerThread(1, "Thread-1")
consumer = consumerThread(2, "Thread-2")

# Start new Threads
producer.start()
consumer.start()

# Add threads to thread list
threads.append(producer)

threads.append(consumer)

# Wait for all threads to complete
for t in threads:
    t.join()
print "Exiting Main Thread"