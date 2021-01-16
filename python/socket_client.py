from threading import *
from socket import *
from time import *
#from serial import *

print (active_count())
print (enumerate()) #和后面返回结果一样，只不过这里是列表形式
print (current_thread())

all_data=b""
def datasend():
    global c,all_data,threadLock,dns_ip
    try:
        threadLock.acquire()
        c.send(all_data)
    except Exception as e:
        print("---异常---：", e)
    finally:
        pass
    all_data=b""
    threadLock.release()
    sleep(0.3)

def datarecv():
    global c,all_data,threadLock,dns_ip
    try:
        threadLock.acquire()
        all_data=c.recv(1024)
    except Exception as e:
        print("---异常---：", e)
    finally:
        pass
    threadLock.release()
    if not all_data:
        print ("对方已断开链接")
        while True:
            try:
                c.close()
                c=socket(AF_INET,SOCK_STREAM,0)
                c.connect(dns_ip)
            #except ConnectionRefusedError:
                #print("服务器未打开")
            except Exception as e:
                print("---异常---：", e)
            break
    sleep(0.3)
    
def socketopen():
    global c,threadLock,dns_ip
    c=socket(AF_INET,SOCK_STREAM,0)
    dns_ip=("127.0.0.1",10000)
    try:
        c.connect(dns_ip)
    except ConnectionRefusedError:
        print("服务器未打开")
    except Exception as e:
        print("---异常---：", e)
    while True:
        sendid=Thread(target = datasend, args = (), name = 'send')
        recvid=Thread(target = datarecv, args = (), name = 'recv')

        sendid.start()
        recvid.start()
        sleep(0.3)
    
if __name__=="__main__":
    global threadLock
    threadLock = Lock()
    socketid=Thread(target = socketopen, args = (), name = 'socket')
    socketid.start()
    
        
        