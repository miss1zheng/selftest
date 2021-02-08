import serial
serial_fail=False
def serialopen():
  global serial_fail
  try: #异常捕获，如其他串口工具已经打开此串口则会异常
    ser=serial.Serial("com75",115200,timeout=0.5) #打开串口，参1不能是整型，timeout会影响下面的 read/readline/ 读取（时间到来之后才输出，过小可能导致未接收数据）
  except serial.SerialException:
    serial_fail=True
  finally:
    pass
  if serial_fail:
    print ("串口打开失败，请检查串口是否存在或串口已在其他地方打开！")
    return
  if (ser.isOpen()):
    print ("端口已打开")
  else:
    ser.open() #在Serial最好设置timeout，因为后面while循环，若不设置默认为None永久等待，执行到此处已打开时若不设置则会一直阻塞下去
  c=ser.write(("ATI\r\n").encode()) #encode()默认为utf-8
  while True:
    s=ser.read(10)#在timeout到来之前读取到数据并在超时时间之内可多次接收数据，超过超时时间无数据输入则会进入break退出
    try:#编码格式输出异常
      print (s.decode(),end="")
    except UnicodeDecodeError:
      print (s.decode('gbk'),end="") #加个end可以使输出的数据不换行
    if not s: #没有数据读取了
      break
  print ("read ok.")
  ser.close()
if __name__=="__main__":
  serialopen()
