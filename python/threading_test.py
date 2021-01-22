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
print(threading.local()) #线程本地数据，class threading.local：一个代表线程本地数据的类。
print("threading end...")

lock = threading.Lock()
lock.acquire()
print("enter lock.")
lock.release()
print("exit lock.")
lock.acquire()
print("enter lock again.")
lock.release()
print("exit lock again.")


rLock = threading.RLock()
rLock.acquire()
print("enter rlock.")
rLock.acquire()
print("enter rlock again.")
rLock.release()
print("exit rlock.")
rLock.release()
print("exit lock again.")
'''

'''
import threading
import time


num = 0
con = threading.Condition()


class Producer(threading.Thread):
    """生产者"""
    def run(self):
        global num
        # 获取锁
        con.acquire()
        while True:
            num += 1
            print('生产了1个，现在有{0}个'.format(num))
            time.sleep(1)
            if num >= 5:
                print('已达到5个，不再生产')
                # 唤醒消费者
                con.notify()
                # 等待-释放锁；被唤醒-获取锁
                con.wait()
        # 释放锁
        con.release()


class Customer(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.money = 7

    def run(self):
        global num
        while self.money > 0:
	        # 由于场景是多个消费者进行抢购，如果将获取锁操作放在循环外(如生产者),
	        # 那么一个消费者线程被唤醒时会锁住整个循环，无法实现另一个消费者的抢购。
	        # 在循环中添加一套"获取锁-释放锁",一个消费者购买完成后释放锁，其他消费者
	        # 就可以获取锁来参与购买。
            con.acquire()
            if num <= 0:
                print('没货了，{0}通知生产者'.format(
                    threading.current_thread().name))
                con.notify()
                con.wait()
            self.money -= 1
            num -= 1
            print('{0}消费了1个, 剩余{1}个'.format(
                threading.current_thread().name, num))
            con.release()
            time.sleep(1)
        print('{0}没钱了-回老家'.format(threading.current_thread().name))


if __name__ == '__main__':
    p = Producer(daemon=True)
    c1 = Customer(name='Customer-1')
    c2 = Customer(name='Customer-2')
    p.start()
    c1.start()
    c2.start()
    c1.join()
    c2.join()
'''
'''
import threading,time
from random import randint
class Producer(threading.Thread):
    def run(self):
        global L
        while True:
            val=randint(0,100)
            # print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
            print('生产者',self.name,' Append'+str(val),L)
            if lock_con.acquire():
                L.append(val)
                lock_con.notify()
                lock_con.release()
            time.sleep(3)
class Consumer(threading.Thread):
    def run(self):
        global L
        while True:
            lock_con.acquire()
            if len(L)==0:
                lock_con.wait()
            print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
            print('消费者',self.name,'Delete'+str(L[0]),L)
            del L[0]
            lock_con.release()
            time.sleep(0.5)
if __name__=='__main__':
    L=[]
    lock_con=threading.Condition()
    threads=[]
    for i in range(5):
        threads.append(Producer())
    threads.append(Consumer())
    for t in threads:
        t.start()
    for t in threads:
        t.join()
'''
'''
import time

num=0
def add():
    global num,conid
    while True:
        conid.acquire()
        num +=2
        print("num add,and num is",num)
        conid.notify()
        conid.wait()
        conid.release()
        if num>10:
            break

def sub():
    global num,conid
    while True:
        conid.acquire()
        num -= 1
        print("num sub,and num is",num)
        conid.notify()
        conid.wait()
        conid.release()
        if num>10:
            break
    
conid=threading.Condition()
sendid=threading.Thread(target=add,name="add",daemon=True)
recvid=threading.Thread(target=sub,name="sub")
sendid.start()
recvid.start()
sendid.join(timeout=10)
recvid.join(timeout=10)

print("threading end...")
'''

'''
import threading
import time
data=0
num=20
def getnumber():
    global cond,data
    time.sleep(1) 
    cond.acquire()
    print ("input your number:")
    data=int(input(">>>"))
    cond.notify()
    cond.wait(timeout=10)
    print ("ok.you are very good.")
    cond.notify()
    cond.release()

def setnumber():
    global cond,data,num
    cond.acquire()
    cond.wait()
    if(data < num):
        cond.notify()
        cond.release() 
    else:
        print ("you wait please.ok.number is ok.")
        temp=0
        for i in range(num,data):
            temp +=2
        num += temp
        temp=0
        cond.notify()
        cond.wait()
        print("thanks.")
        cond.release() 
        
cond = threading.Condition()
setid=threading.Thread(target=setnumber,name="set")
getid=threading.Thread(target=getnumber,name="get")
setid.start()
getid.start()
'''
'''
import threading
import time
num=0
def frist():
    while True:
        global num,even
        if num <10:
            even.clear()
            for i in range(15):
                num = num + 2
        if num >0:
            even.set()
        print("frist number is",num)
        time.sleep(0.5)

def second():
    while True:
        global num,even
        if (num>8) and even.is_set():
            num -= 8
            print("second number is",num)
        if (num<8):
            print("haven't numer.please add number.")
        time.sleep(0.5)
    
def thrid():
    while True:
        global num,even
        if (num>5) and even.is_set():
            num -= 5
            print("thrid number is",num)
        if (num<5):
            print("haven't numer.please add number.")
            
        time.sleep(0.5)

if __name__=="__main__":
    even = threading.Event()
    fristid = threading.Thread(target=frist)
    secondid = threading.Thread(target=second)
    thridid = threading.Thread(target=thrid)
    fristid.start()
    secondid.start()
    thridid.start()
    fristid.join()
    secondid.join()
    thridid.join()
'''
'''
import threading
import time
num1=0
num2=0
num3=0
def frist():
    global num1,sem
    print("enter frist...")
    sem.acquire()
    while True:
        if num1 <10:
            num1 += 4
            print("frist num:",num1)
        else:
            sem.release()
            print("...exit frist")
            break
        time.sleep(0.5)

def second():
    global num2,sem
    print("enter second...")
    sem.acquire()
    while True:
        if num2 <30:
            num2 += 10
            print("second num:",num2)
        else:
            sem.release()
            print("...exit second")
            break
        time.sleep(0.5)
    
def thrid():
    global num3,sem
    print("enter thrid...")
    sem.acquire()
    while True:
        if num3 < 20:
            num3 += 8
            print("thrid num:",num3)
        else:
            sem.release()
            print("...exit thrid")
            break
        time.sleep(0.5)

if __name__=="__main__":
    sem = threading.Semaphore(2)
    fristid = threading.Thread(target=frist)
    secondid = threading.Thread(target=second)
    thridid = threading.Thread(target=thrid)
    fristid.start()
    secondid.start()
    thridid.start()
'''
'''
import time
import threading
def callback():
    print("  end time is:",time.asctime( time.localtime(time.time()) ))
if __name__=="__main__":
    print("start time is:",time.asctime( time.localtime(time.time()) ))
    timeid = threading.Timer(5,callback)
    timeid.start()
'''