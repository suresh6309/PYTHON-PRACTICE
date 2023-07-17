#multi threading
#link in https://codeshare.io/vwnBrD
import threading
import time
def show(threadname,delay,n):
    count=0
    while count<n:
        time.sleep(delay)
        count+=1
        print('{}-{}'.format(threadname,time.ctime(time.time())))
t1=threading.Thread(target=show,args=(T1,2,5))
t2=threading.Thread(target=show,args=(T2,1,5))
t1.start()
t2.start()
#whithout threading
#show('T1,2,5')
#show('T1,1,5')
