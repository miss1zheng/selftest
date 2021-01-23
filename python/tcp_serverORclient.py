import threading
import socket
def TcpServer():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
    host = socket.gethostname()
    port = 10000
    s.bind((host, port))
    s.listen(1)
    while True:
        c,addr = s.accept()
        print ('客户端连接地址：', addr)
        while True:
            data=c.recv(1024)
            c.send(data)
        c.close()
    s.close()

def TcpClient():
    c=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
    host = socket.gethostname()
    try:
        c.connect((host,10000))
    except ConnectionRefusedError:
        print("服务器端未打开，服务器拒绝连接.")
    while True:
        data=input(">>>").encode('gbk')
        c.send(data)
        recvdata=c.recv(1024)
        print("<<<",recvdata.decode('gbk'))

def TCPOPEN():
    while True:
        enserver=input("TCPSERVER?1(YES)/0(NO)?")
        if enserver=="0":
            print("TCP Client start...")
            tcpclient=threading.Thread(target=TcpClient,name="server")
            tcpclient.start()
            tcpclient.join()
        elif enserver=="1":
            print("TCP Server start...")
            tcpserver=threading.Thread(target=TcpServer,name="server")
            tcpserver.start()
            tcpserver.join()
        else:
            print("you input data error,you need intput again.please")
       
if __name__=="__main__":
    oneid=threading.Thread(target=TCPOPEN,name="tcpopen")
    oneid.start()
    oneid.join()
