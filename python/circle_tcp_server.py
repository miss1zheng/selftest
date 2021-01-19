# -*- coding: UTF-8 -*-

from socket import *
from time import *
from threading import *

data=b''
socket_en=False
def datarecv(c):
    global data,threadLock,socket_en
    threadLock.acquire()
    try:
        data=c.recv(1024)
    except Exception as e:
        pass
    threadLock.release()
    if not data:
        socket_en=False
    sleep(0.2)
def datasend(c):
    global data,threadLock,socket_en
    threadLock.acquire()
    try:
        c.send(data)
    except Exception as e:
        socket_en=False
    threadLock.release()
    data=b''
    sleep(0.2)
def socketopen():
    global socket_en
    s = socket(AF_INET,SOCK_STREAM,0)         # 创建 socket 对象
    host = gethostname() # 获取本地主机名
    port = 10000                # 设置端口
    s.bind((host, port))        # 绑定端口
    s.listen(1)                 # 等待客户端连接
    while True:
        c,addr = s.accept()     # 建立客户端连接
        print ('连接地址：', addr)
        socket_en=True
        while True:
            recvid=Thread(target = datarecv, args = (c,), name = 'recv', daemon=True)
            sendid=Thread(target = datasend, args = (c,), name = 'send', daemon=True)
            recvid.start()
            sendid.start()
            if socket_en==False:
                print("客户端已断开")
                c.close()
                break
            sleep(0.3)
        sleep(0.3)
    s.close()
    
if __name__=="__main__":
    global threadLock
    threadLock = Lock()
    socketid=Thread(target = socketopen, args = (), name = 'socket')
    socketid.start()
