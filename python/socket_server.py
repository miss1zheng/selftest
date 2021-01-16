# -*- coding: UTF-8 -*-

from socket import *
from time import *
from threading import *

clist=[]
def socketopen():
    s = socket()         # 创建 socket 对象
    host = gethostname() # 获取本地主机名
    port = 10000                # 设置端口
    while True:
        s.bind((host, port))        # 绑定端口
        s.listen(5)                 # 等待客户端连接
        while True:
            c,addr = s.accept()     # 建立客户端连接
            print ('连接地址：', addr)
            clist.append(c)
            while True:
                data=c.recv(1024)
                if not data:
                    print("客户端已断开")
                    break
                else:
                    print(data)
                    c.send(data)
                sleep(0.3)
            sleep(0.3)
        sleep(0.3)
    sleep(0.3)
    
if __name__=="__main__":
    socketid=Thread(target = socketopen, args = (), name = 'socket')
    socketid.start()
    sleep(0.3)

'''
import socket
import sys

Clients=[]#创建客户端socket列表

def main():
    #创建socket 对象
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    localAddr=('',8080)
    server_socket.bind(localAddr)# 绑定端口号
    server_socket.listen(5)# 设置最大连接数，超过后排队
    server_socket.setblocking(0)#将套接字设置为非堵塞　　
    while True:
        try:
            newClient=server_socket.accept()
        except Exception as result:#如果没有客户端连接则产生一个异常
            pass
        else:#如果有客户端连接，则将新的客户端设置为非阻塞，并添加到客户端列表中
            newClient[0].setblocking(0)
            Clients.append(newClient)
        Clients_invalid=[]#创建无效的客户端列表
        for clientSocket,clientAddr in Clients:
            try:
                meg='0'
                clientSocket.send(msg.encode('utf-8'))#通过发送数据判断客户端是否在线
            except Exception as e:#客户端不在线
                clientSocket.close()#关闭连接
                Clients_invalid.append((clientSocket,clientAddr))#将客户端计入无效列表
            else:
                try:
                    recvData=clientSocket.recv(1024)
                    if len(recvData)>0:
                        print(recvData)#处理数据
                    else:
                        pass
                except :#接收异常则忽略
                    pass
        for client in Clients_invalid:#从客户端列表中移除无效的客户端
            Clients.remove(client)
if __name__=='__main__':
    main()
'''