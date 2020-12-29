import socket
import threading
import time
import tkinter

def senddata(name,s):
    print("start %s..." % (name))
    while True:

        #s.send(sendstr.get().encode())
        try:
            s.send("".encode("gbk"))
        except ConnectionAbortedError:
            print ("客户端已断开")
            s.close()
            break
        time.sleep(0.2)
def recvdata(name,s):
    print("start %s..." % (name))
    while True:
        try:
            data=s.recv(1024)
        except OSError:
            print ("客户端已断开")
            s.close()
            break
        print (data)
        if data == b'':
            try:
                s.send("心跳".encode("gbk"))
            except ConnectionAbortedError:
                print ("客户端已断开")
                s.close()
                break
            finally:
                pass
        else:
            print ("recv data:",data.decode("gbk"))
        #recvtext.insert(1.0,s.recv(1024))
        time.sleep(0.2) 
def tcpserver():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
    s.bind(('127.0.0.1',10000))#s.bind(('localhost',10000))
    s.listen(10)
    alladdr=[]
    while True:
        c,addr=s.accept()
        if addr == "":
            alladdr.append(addr)
        else:
            for i in range(len(alladdr)):
                if addr != i:
                    alladdr.append(addr)
        print (addr)
        send=threading.Thread(target=senddata, args=("sendThread",c),daemon=True )
        recv=threading.Thread(target=recvdata, args=("recvThread",c),daemon=True)
        #send.setName("sendThread")
        #recv.setName("recvThread")
        send.start()
        recv.start()
        send.join()   # 等待子线程运行结束
        recv.join()
        time.sleep(1)
    s.close()

if __name__=="__main__":   
    tcpserver()
    
    