import os, sys
from stat import *

ERROR_COUNT = 0
def walktree(top):
    global ERROR_COUNT
    '''recursively descend the directory tree rooted at top,
       calling the callback function for each regular file'''

    for f in os.listdir(top):
        try:
            pathname = os.path.join(top, f)
            mode = os.stat(pathname).st_mode
            if S_ISDIR(mode):
                # It's a directory, recurse into it
                walktree(pathname)
            elif S_ISREG(mode):
                # It's a file, call the callback function
                byte_size = os.stat(pathname).st_size
                link_count = os.stat(pathname).st_nlink
                print pathname, 'has bytes==>', byte_size
                if link_count > 1:
                    print 'Found', link_count, 'hard links for', pathname
            else:
                # Unknown file type, print a message
                print 'Skipping %s' % pathname
        except Exception as e:
            pass


if __name__ == '__main__':
    walktree(sys.argv[1])
    print ERROR_COUNT