import threading
'''
import time
num=0
def callbackfunct(b):
    global num
    print ("this is a thread...")
    while True:
        for i in range(0,b):
            num +=i
        print("add is ",num)
        if num > 100:
            break
        time.sleep(6)
a=10
threadid=threading.Thread(target=callbackfunct,name='add',args=(a,),daemon=True)
print("num is ",num)
print("name is ",threadid.name,",alive is ",threadid.is_alive(),",daemon is ",threadid.daemon)
threadid.setName("charge_name")
threadid.setDaemon(False)
print("name is ",threadid.getName(),",alive is ",threadid.is_alive(),",daemon is ",threadid.isDaemon())
threadid.start()
print("name is ",threadid.getName(),",alive is ",threadid.is_alive(),",daemon is ",threadid.isDaemon())
threadid.join(timeout=5)
print("name is ",threadid.name,",alive is ",threadid.is_alive(),",daemon is ",threadid.daemon)
print("num is ",num)


print(threading.active_count) #返回当前存活的线程类 Thread 对象，返回的计数等于 enumerate() 返回的列表长度。
print(threading.enumerate()) #返回当前存活的线程类 Thread 对象, 该列表包含守护线程，current_thread() 创建的虚拟线程对象和主线程。它不包含已终结的线程和尚未开始的线程。
print(threading.current_thread()) #返回当前对应调用者的控制线程的 Thread 对象。如果调用者的控制线程不是利用 threading 创建，会返回一个功能受限的虚拟线程对象。
print(threading.get_ident()) #返回当前线程的 “线程标识符”。它是一个非零的整数。
print(threading.main_thread()) #返回主 Thread 对象。一般情况下，主线程是Python解释器开始时创建的线程。

num=0
num1=0
def callback_thread_main():
    global lockid,num
    print("start settrace...")
    for i in range(0,10):
        num += 1
    print("num is ",num)
    
threading.settrace(callback_thread_main()) #为所有 threading 模块开始的线程设置追踪函数。在每个线程的 run() 方法被调用前，func 会被传递给 sys.settrace() 。

def callback_main():
    global lockid,num1
    print("start setprofile...")
    for i in range(0,10):
        num1 += 1
    print("num1 is ",num)
    
threading.setprofile(callback_main()) #为所有 threading 模块开始的线程设置性能测试函数。在每个线程的 run() 方法被调用前，func 会被传递给 sys.setprofile() 。

threading.stack_size(32768) #至少32768自己，32k
threading.TIMEOUT_MAX #阻塞函数（ Lock.acquire(), RLock.acquire(), Condition.wait(), …）中形参 timeout 允许的最大值。传入超过这个值的 timeout 会抛出 OverflowError 异常。

print(threading.local()) #线程本地数据，class threading.local：一个代表线程本地数据的类。
print("lock is blocking.")
print("lock is deblocking.")
'''
import time
senda=["start send data.","send data success."]
recva=["start recv data.","recv data success."]
data=""
def senddata():
    global senda,data,conid
    conid.acquire()
    data=senda[0]
    conid.notify()
    conid.wait()
    time.sleep(0.5)
def recvdata():
    global recva,data,conid
    conid.acquire()
    conid.wait()
    data=recva[0]
    conid.notify()
    time.sleep(0.5)
def alldata():
    global data
    while True:
        print (">>>",data)
        time.sleep(0.2)
conid=threading.Condition()
sendid=threading.Thread(target=senddata,name="send",daemon=True)
recvid=threading.Thread(target=recvdata,name="recv",daemon=True)
allid=threading.Thread(target=alldata,name="all")
sendid.start()
recvid.start()
allid.start()
time.sleep(0.2)
sendid.join()
recvid.join()
alldata.join()


conid.acquire()
conid.release()
conid.wait()
conid.wait_for()
conid.notify()
conid.notify_all()



print("threading end...")



