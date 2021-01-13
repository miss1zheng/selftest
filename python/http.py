import httplib
import socket
import time

s = socket.socket()         # 创建 socket 对象
host = socket.gethostname() # 获取本地主机名
port = 9090                # 设置端口号
 
s.connect((host, port))
while True:
    print s.recv(1024)
    time.sleep(1000)
    s.send("client send data")
s.close()
