import httplib
import socket
import time

s = socket.socket()         # ���� socket ����
host = socket.gethostname() # ��ȡ����������
port = 9090                # ���ö˿ں�
 
s.connect((host, port))
while True:
    print s.recv(1024)
    time.sleep(1000)
    s.send("client send data")
s.close()
