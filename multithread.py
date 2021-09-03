import time
import threading

def print_time(threadName,delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))

if __name__ == '__main__':
    t1 = threading.Thread(target=print_time, args=("T1",5))
    t2 = threading.Thread(target=print_time, args=("T2",10))
    t1.start()
    t2.start()
    print("No. of active threads: " + str(threading.active_count()))
    #t1.join()
    #t2.join()