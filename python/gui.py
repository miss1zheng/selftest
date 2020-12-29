'''
this is main project,All functions start here
'''
import sys
import time
import os
import socket
import binascii
from tkinter import *
from tkinter.messagebox import *
from tkinter import filedialog
from threading import Thread


win=Tk()

start_en=False
def center_window(r,w, h):
	ws = r.winfo_screenwidth()
	hs = r.winfo_screenheight()
	x = (ws/2) - (w/2)
	y = (hs/2) - (h/2)
	r.geometry("%dx%d+%d+%d" % (w, h, x, y))





############
#socket实现
#############
tcps_en=False
tcpc_en=False
udps_en=False
udpc_en=False
def tcpc_conn():
	if tcpc_en==True:
		while True:
			global win,tcpudpip,tcpudpport,g_socket,socksend,sockrecv
			ip=tcpudpip.get()
			port=tcpudpport.get()
			g_socket=socket.socket()
			g_socket.connect((ip,int(port)))
			while True:
				tr = Thread(target=tcpc_recv,args=(socksend),daemon=True)
				ts = Thread(target=tcpc_send,args=(sockrecv))#args=(g_socket, (ip,int(port)))
				tr.start()
				ts.start()
			time.sleep(1)
def tcpc_send(socksend):
	global g_socket,send_en
	if send_en==True:
		data=socksend.get(0.0,END)
		print ("send data is ",data)
		g_socket.send(data)
		send_en=False
	time.sleep(1)
def tcpc_recv(sockrecv):
	global g_socket
	recv_data=g_socket.recv(1024)
	sockrecv.insert(1.0,recv_data)
	time.sleep(2)

############
#socket编辑界面
#############
tcpudpip=StringVar()
tcpudpport=StringVar()
g_socket=None
socket_tcps_num=[]
circle_en=False
send_en=False
def tcpudp_socket():#此功能暂时无法实现
	global win,tcpudpip,tcpudpport
	global sock_ip,socket_ip,sock_port,socket_port,sockets_button,socksend,sock_send,sockrecv,sock_recv,socketc_button,allclose_button,circle_button
	sock_ip=Label(win,text='ip',font=('arial',14))
	socket_ip=Entry(win,textvariable=tcpudpip,show=None,font=('arial',14))
	sock_port=Label(win,text='port',font=('arial',14))
	socket_port=Entry(win,textvariable=tcpudpport,show=None,font=('arial',14))
	sock_send=Button(win,text = 'send',width = 10,height =1,command=send_start)
	sock_recv=Label(win,text='recv',font=('arial',14))
	socketc_button=Button(win,text = 'close',width = 10,height =1,command=socket_close)
	allclose_button=Button(win,text = 'all close',width = 10,height =1,command=tcpudp_close)
	circle_button=Button(win,text = 'circle',width = 10,height =1,command=circleset)	
	sockrecv=Text(win, height=40)
	socksend=Text(win, height=4)

	global socktcps_label,socktcpc_label,sockudps_label,sockudpc_label,sockettcps_button,sockettcpc_button,socketudps_button,socketudpc_button
	socktcps_label=Label(win,text='tcp server',font=('arial',14))
	socktcpc_label=Label(win,text='tcp client	',font=('arial',14))
	sockudps_label=Label(win,text='udp server',font=('arial',14))
	sockudpc_label=Label(win,text='udp client	',font=('arial',14))
	sockettcps_button=Button(win,text = 'start',width = 10,height =1,command=tcps)
	sockettcpc_button=Button(win,text = 'start',width = 10,height =1,command=tcpc)
	socketudps_button=Button(win,text = 'start',width = 10,height =1,command=udps)
	socketudpc_button=Button(win,text = 'start',width = 10,height =1,command=udpc)

def tcpudp_open(name):
	global sock_ip,socket_ip,sock_port,socket_port,socksend,sock_send,sockrecv,sock_recv,socketc_button,allclose_button,circle_button
	global socktcps_label,socktcpc_label,sockudps_label,sockudpc_label,sockettcps_button,sockettcpc_button,socketudps_button,socketudpc_button
	sock_ip.place(x=0,y=40)
	socket_ip.place(x=50,y=40)
	sock_port.place(x=0,y=70)
	socket_port.place(x=50,y=70)
	allclose_button.place(x=500,y=50)
	socketc_button.place(x=150,y=100)
	socksend.place(x=0,y=140)
	sock_send.place(x=0,y=200)
	sock_recv.place(x=0,y=280)
	sockrecv.place(x=0,y=310)
	if name=='tcps':
		circle_button.place(x=250,y=100)
		socktcps_label.place(x=50,y=0)
		sockettcps_button.place(x=50,y=100)
	elif name=='tcpc':
		circle_button.place_forget()
		socktcpc_label.place(x=50,y=0)
		sockettcpc_button.place(x=50,y=100)	
	elif name=='udps':
		circle_button.place(x=250,y=100)
		sockudps_label.place(x=50,y=0)
		socketudps_button.place(x=50,y=100)
	elif name=='udpc':
		circle_button.place_forget()
		sockudpc_label.place(x=50,y=0)
		socketudpc_button.place(x=50,y=100)
		

def tcpudp_close():
	global sock_ip,socket_ip,sock_port,socket_port,socksend,sock_send,sockrecv,sock_recv,circle_button,socketc_button,allclose_button
	sock_ip.place_forget()
	socket_ip.place_forget()
	sock_port.place_forget()
	socket_port.place_forget()
	socketc_button.place_forget()
	allclose_button.place_forget()
	circle_button.place_forget()
	socksend.place_forget()
	sock_send.place_forget()
	sock_recv.place_forget()
	sockrecv.place_forget()
	global sockettcps_button,sockettcpc_button,socketudps_button,socketudpc_button,socktcps_label,socktcpc_label,sockudps_label,sockudpc_label
	sockettcps_button.place_forget()
	sockettcpc_button.place_forget()
	socketudps_button.place_forget()
	socketudpc_button.place_forget()
	socktcps_label.place_forget()
	socktcpc_label.place_forget()
	sockudps_label.place_forget()
	sockudpc_label.place_forget()

def socket_close():
	if g_socket!=None:
		g_socket.close()
		for i in range(5):
			del socket_tcps_num[i]
	send_en=False

def circleset():
	circle_en=True
def send_start():
	send_en=True

def socket_tcps():
	tcpudp_open('tcps')
def tcps():
	global win,tcpudpip,tcpudpport,g_socket
	ip=tcpudpip.get()
	port=tcpudpport.get()
	g_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	g_socket.bind((ip,int(port)))
	g_socket.listen(5)
	while True:
		print ("waiting for connection.....")
		c,addr=s.accept()
		print ("connect from:",addr)
		##下面的wile适用于循环功能
		if circle_en==True:
			while True:
				data=c.recv(1024)
				if not data:
					print ("recv data have not data.")
				print (">>>%s:%s" % (addr,data))
				if not data:
					c.send("no data")
				else:
					c.send(data)

def socket_tcpc():
	tcpudp_open('tcpc')
def tcpc():
	tcpc_en=True

def socket_udps():
	tcpudp_open('udps')
def udps():
	global win,tcpudpip,tcpudpport
	ip=tcpudpip.get()
	port=tcpudpport.get()
	g_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM,0)
	g_socket.bind((ip,int(port)))
	while True:
		data,addr=g_socket.recvfrom(1024)
		print ('received from %s:%s' % (addr,data))
		if not data:
			senddata=g_socket.sendto("pelease you send data.",addr)
			print (senddata)
		elif data=='kill':
			g_socket.close()
			exit()
			break
		else:
			senddata=g_socket.sendto(data,addr)
			print (senddata)
			print ('data and ip is %s:%s' % (addr,data))

def socket_udpc():
	tcpudp_open('udpc')
def udpc():
	global win,tcpudpip,tcpudpport,sockrecv
	circle_button.place_forget()
	ip=tcpudpip.get()
	port=tcpudpport.get()

	while True:
		senddata=raw_input(">>>")
		g_socket= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		g_socket.sendto(senddata, ((ip,int(port))))
		data,addr = g_socket.recvfrom(1024)
		print (data)
		del senddata






#############
#文件编辑功能，file edit/open/save
#############
edit_en = False
def file_start(name):
	global edit_text,edit_en
	#edit_text=Text(win,width=600,height=600)
	if name == 'edit':
		edit_en = True
		edit_text.place(x=0,y=0)
	elif name == 'open':
		filename=filedialog.askopenfilename(title=u'open file')#返回值为路径与文件名
		with open(""+filename,'r') as f:
			edit_text.insert(1.0,f.read())
		edit_en = True
		edit_text.place(x=0,y=0)
	elif (name == 'save') and (edit_en == True):
		edit_text.place(x=0,y=0)
		edit_info=edit_text.get(0.0,END)
		fname=filedialog.asksaveasfilename(title=u'save file')
		with open(fname,'w') as file:
			file.write(edit_info)
	elif name == 'close':
		edit_en = False
		edit_text.place_forget()
	else:
		print ("other ,", name,",,",edit_en)

def edit_start():
	file_start('edit')

def open_start():
	file_start('open')

def save_start():
	file_start('save')

def close_start():
	file_start('close')


##############
#crc校验
#############
import zlib
def crc_menu():
	global win,crc8_label,crc32_label,crc8_button,crc32_button,crc_text,crcsul_text,crcresul_label
	crc8_label=Label(win,text='crc8',font=('arial',14))
	crc32_label=Label(win,text='crc32',font=('arial',14))
	crc8_button=Button(win,text = 'start',width = 10,height =1,command=crc8_value)
	crc32_button=Button(win,text = 'start',width = 10,height =1,command=crc32_value)
	crc_text=Text(win,height=12)
	crcsul_text=Text(win,height=2)
	crcresul_label=Label(win,text='result',font=('arial',14))
	
def crc8_open():
	global crc8_label,crc8_button,crc_text,crcsul_text,crcresul_label
	#crc8_label.place_forget()
	crc8_label.place(x=10,y=0)
	crc8_button.place(x=10,y=200)
	crc_text.place(x=10,y=30)
	crcsul_text.place(x=10,y=250)
	crcresul_label.place(x=10,y=280)

def crc8_value():
	pass

def crc32_open():
	global crc32_label,crc32_button,crc_text,crcsul_text,crcresul_label
	#crc8_label.place_forget()
	crc32_label.place(x=0,y=0)
	crc32_button.place(x=10,y=200)
	crc_text.place(x=10,y=30)
	crcsul_text.place(x=10,y=250)
	crcresul_label.place(x=10,y=280)

def crc32_value():#不能是中文
	global crc_text,crcsul_text
	data=(crc_text.get('0.0',END)).replace('\n', '')#去除文本获取时会获取最后一个\n换行符
	adata=data.encode('utf-8')#encode为字符串转成字节流，而decode为字节流转成字符串(字节流可以保存到磁盘或在网络上传输)
	result=binascii.crc32(adata)&0xffffffff
	#result=zlib.crc32(adata)&0xffffffff#和上面一样的功能
	b=hex(result)
	crcsul_text.delete(1.0,END)
	crcsul_text.insert(1.0,b)


##########
#菜单界面 menu start...
##########
def start():
	pass

def menuface():
	global start_en,win
	if start_en != True:
		return

	menubar=Menu(win)
	filemenu=Menu(menubar,tearoff=0)

	global edit_text
	edit_text=Text(win,width=600,height=600)
	menubar.add_cascade(label='File',menu=filemenu)
	filemenu.add_command(label='Edit',command=edit_start)
	filemenu.add_command(label='Open',command=open_start)
	filemenu.add_command(label='Save',command=save_start)
	filemenu.add_command(label='Close',command=close_start)
	submenu=Menu(filemenu)
	filemenu.add_cascade(label='Edit View',menu=submenu,underline=0)
	submenu.add_command(label='colour',command=start)
	submenu.add_command(label='form',command=start)
	submenu.add_separator()
	submenu.add_command(label='size',command=start)

	tcpudp_socket()
	funtmenu=Menu(menubar,tearoff=0)
	menubar.add_cascade(label='Function',menu=funtmenu)
	submenu=Menu(funtmenu)
	funtmenu.add_cascade(label='Socket',menu=submenu,underline=0)
	submenu.add_command(label='TCP Server',command=socket_tcps)
	submenu.add_command(label='TCP Client',command=socket_tcpc)
	submenu.add_separator()
	submenu.add_command(label='UDP Server',command=socket_udps)
	submenu.add_command(label='UDP Client',command=socket_udpc)

	crc_menu()
	submenu=Menu(funtmenu)
	funtmenu.add_cascade(label='CRC',menu=submenu,underline=0)
	submenu.add_command(label='crc16 modbus',command=start)
	#submenu.add_separator()
	submenu.add_command(label='crc32',command=crc32_open)
	submenu.add_command(label='crc8',command=crc8_open)

	win.config(menu=menubar)







##########
# 登录界面 login start...
##########
user_name=StringVar()
pass_word=StringVar()
user_info={'admin':'admin'}
def log_in():
	global user_name,pass_word,start_en
	username=user_name.get()
	password=pass_word.get()
	if username in user_info:
		if password==user_info[username]:
			start_en=True
			delete_frame()
			menuface()
			return
		else:
			askokcancel("提示","log in fail.password is err.")
			start_en=False
	else:
		#askokcancel("提示","log in is fail.username is error.")
		askokcancel("提示","log in fail.username is err.")
		start_en=False

def sign_up():
	global user_name,pass_word,start_en
	username=user_name.get()
	password=pass_word.get()
	#if user_info.has_key(username) == True:
	if username in user_info:
		askokcancel("提示","there be username.please restart input.")
	else:
		user_info[username]=password
		start_en=True
		delete_frame()
		menuface()

def user_delete():
	global user_name,pass_word,start_en
	username=user_name.get()
	password=pass_word.get()
	if username in user_info:
		if password==user_info[username]:
			#askokcancel("提示","delete is success.")
			askokcancel("提示","delete succ.")
			del user_info[username]
			start_en=False
		else:
			askokcancel("提示","delete fail.password err.")
	else:
		askokcancel("提示","delete fail.username err.")

def login():
	#while True:
	global start_en,win
	if start_en!=False:
		return
	global name_label,name_entry,pswd_label,pswd_entry,login_button,sinup_button,usrdel_button,test_button
	name_label=Label(win,text='username',font=('arial',14))
	name_entry=Entry(win,textvariable=user_name,show=None,font=('arial',14))
	pswd_label=Label(win,text='password',font=('arial',14))
	pswd_entry=Entry(win,textvariable=pass_word,show='*',font=('arial',14))
	login_button=Button(win,text='log in',command=log_in)
	sinup_button=Button(win,text='sign up',command=sign_up)
	usrdel_button=Button(win,text='delete user',command=user_delete)
	start_frame()

	test_button=Button(win,text='test',command=user_test)
	test_button.place(x=200,y=180)
	time.sleep(1)

def user_test():
	global start_en,test_button
	start_en=True
	delete_frame()
	menuface()
	test_button.place_forget()

def delete_frame():
	global name_label,name_entry,pswd_label,pswd_entry,login_button,sinup_button,usrdel_button
	name_label.place_forget()
	name_entry.place_forget()
	pswd_label.place_forget()
	pswd_entry.place_forget()
	login_button.place_forget()
	sinup_button.place_forget()
	usrdel_button.place_forget()

def start_frame():	
	name_label.place(x=0,y=30)
	name_entry.place(x=100,y=30)
	pswd_label.place(x=0,y=60)
	pswd_entry.place(x=100,y=60)
	login_button.place(x=80,y=100)
	sinup_button.place(x=150,y=100)
	usrdel_button.place(x=230,y=100)


def main_test():
	win.title("phn")
	center_window(win,600,600)
	'''
	global sockrecv,socksend
	sockrecv=Text(win, height=40)
	socksend=Text(win, height=4)
	tcps_task = Thread(target=tcpc_conn,daemon=True)
	interface_task = Thread(target=login,daemon=True)#args=(g_socket, (ip,int(port)))
	tcps_task.start()
	interface_task.start()
	'''
	login()
	win.mainloop()

if __name__=='__main__':
	main_test()


