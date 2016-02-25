""" python thread example """

import threading
import time

GBL_COUNT = 0
SHARED_DB = []

class WriterThread(threading.Thread):
    def __init__(self, threadID, name, e):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.runtime = e

    def run(self):
        print "Starting " + self.name
        while self.runtime.is_set():
            threadLock.acquire() 
            write_data()
            threadLock.release() 

class ReaderThread(threading.Thread):
    def __init__(self, threadID, name, e):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.runtime = e

    def run(self):
        print "Starting " + self.name   
        while self.runtime.is_set():
            threadLock.acquire() 
            read_data()
            threadLock.release() 

def write_data():
    global GBL_COUNT

    GBL_COUNT += 1
    time.sleep(.5)
    print '\nw_GBL_COUNT => ', GBL_COUNT



def read_data():
    global GBL_COUNT
    
    GBL_COUNT -= 1           
    time.sleep(.5)
    print '\nw_GBL_COUNT => ', GBL_COUNT
       

""" SETUP """


threadLock = threading.Lock()
runtime_e = threading.Event()
runtime_e.set()

# Create new threads
writer = WriterThread(1, "Writer", runtime_e)
reader = ReaderThread(2, "Reader", runtime_e)

# Start new Threads
writer.start()
reader.start()

# Add threads to thread list
threads = []
threads.append(writer)
threads.append(reader)


# Monitor the main thread listening for CTRL-C which will unset the runtime flag then 
# allowing the threads to exit cleanly, then end the program.
try:
    while 1:
        pass

except KeyboardInterrupt:
    
    print "\nAttempting to close threads."
    runtime_e.clear()
    
    # Wait for all threads to complete
    for t in threads:
        t.join()
    
    print "\n All threads closed."