'''
#!/usr/bin/python
# -*- coding:utf-8 -*-
#前面两个一个是加载编译器，一个是加载编码格式
'''
print ("hello,world.世界"),#print默认是换行的，但是在后面加一个逗号就表示不会换行
okif="if is ok." + \
      "add string"#+为连接两个字符串
okdan=['add','b','class','del','else','if',
           'g','h','item','j','k','l','m','num']
oknum,errnum,endstr,complex_num,longnum=11,22.2,"end",9.34e-36j,0122L#这里为赋值整型，浮点型，字符串三种类型，最后面是一个复数类型
okvalue = errvalue = 1;#多变量赋值

if True:
    print okif[1:14]*2  #下标从0开始，冒号后面为获取的数，所以这里会输出"f is o"，后面*2表示输出两次，即输出"f is of is o"
    print okdan[0]      #只输出此下标字符串
    print okdan[3:]     #下标开始后面的全部输出
    print oknum*2       #即11*2=22
    print okdan[2:9:4]  #截取字符串，即开始一个是下标为2的字符串，然后最后一个为[9-(4+2)]=4，即从下标为9开始向前移动四个位置的字符串
    print okdan[-6]     #读取倒数第6个元素
else:
    print errnum;print("else is end.")
print endstr

#删除一些对象的引用
#print oknum#删除了之后就不能再使用了
del oknum
del errnum,endstr

raw_input("we are used to \"enter\" funtion.")#此函数功能为：按下"enter"键才会执行下面的语句

print "";print "列表";print ""
"""
列表
"""
list=["111","aaa",111,'bbb','222']
otherlist=['hhh',999]
print list
print list[0]
print list[2:]
print list[1:4]
print list*2
print list+otherlist

print "";print "元组";print ""
'''
元组
'''
list=("111","aaa",111,'bbb','222')
otherlist=('hhh',999)
print list
print list[0]
print list[2:]
print list[1:4]
print list*2
print list+otherlist


print "";print "字典";print ""
"""
字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型。列表是有序的对象集合，字典是无序的对象集合。

两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取.
字典用"{ }"标识。字典由索引(key)和它对应的值value组成.
"""
dict={}
dict['one']="this is one"
dict[2]="this is two"
tinydict = {'name':'john','code':7654,'dept':'sales'}
print dict['one']          # 输出键为'one' 的值
print dict[2]              # 输出键为 2 的值
print tinydict             # 输出完整的字典
print tinydict.keys()      # 输出所有键
print tinydict.values()    # 输出所有值

'''
数据类型转换
'''
int('a',16)     #十六进制，值为：10
int('0x0a',16)  #值为：10
int()           #十进制，值为：0
int(3)          #值为：3
int(5.8)        #值为：5.8
int('10',8)     #八进制值为：8

long()          #值为：0L
long(3)         #值为：3L
long('123')     #值为：123L

float()         #值为：0.0
float(134)      #值为：134.0
float(-134.5)   #值为：-134.5
float('134')    #值为：134.0
#复数
complex()       #值为：0j
complex(2,3)    #值为：(2+3j)
complex("1")    #值为：(1+0j)
complex("1+2j") #值为：(1+2j)
#字符串
str()           #值为：''
str('runoob')   #值为：'runoob'
#表达式字符串
repr('runoob')   #值为："'runoob'"
#eval('3*9')
#eval('pow(2,2)')
#tuple([1,2,3,4])
#tuple([1:2,3:4])#字典
#list();set();dict();frozenset();chr();unichr();ord();hex();oct()
#算术运算
print (30-10)*20/10%20#30-10=20x20=400/10=40%20=0
print 20**2//24#400/24=16(实则结果为16.5，不要余数)，其中两个**表示取幂，//表示取整除，整数部分
#比较运算
print 1==1#返回True
print 1!=1
print 1>2
print 1<2
print 1<=2
#赋值运算
a=10;b=20;b+=a;b-=a;b*=a;b/=a;b%=a;b**=a;b//=a
#位运算
a=60;b=13
print a&b
print a|b
print a^b
print ~a
print a<<4
print b<<4
#逻辑运算
a=10;b=20
print (a and b)
print (a or b)
print not(a and b)
#成员运算（如：判断a是否在b列表中），in：元素是否存在列表中
list=["111","aaa",111,'bbb','222']
if(111 in list):
    print '111 in list.'
elif("111" in list):
    print '111 str in list'
elif("bbb" not in list):
    print "bbb not in list"
else:
    print "haven't this value"
#身份运算(is 和 == 区别：用于判断两个变量引用对象是否为同一个(同一块内存空间)， == 用于判断引用变量的值是否相等)
a=10;b=20
if(a is b):
    print "引用同一个对象"
elif(a is not b):
    print "引自不同对象"
#运算符优先级
#条件语句（任何非0或非空null）的值为Ture，为0或空的值为False
num=30
if (num<0 or num>20):
    print "num about over20 or less than 0"
elif(num>0 and num < 5) or (num>10 and num <20):
    print "num about 0-5 or 10-20"
    if(num>0 and num < 5):
        print "num value is 0-5"
    elif(num>10 and num <20):
        print "num value is 10-20"
#循环语句：for、while(任何非0或非空null）的值为Ture，当为false时循环结束)
#break 退出内部循环，continue 用于跳过该次循环(重新开始内部循环)
#pass时空语句不做任何事情，只是为了保持程序结构的完整性，一般用作占位语句，也可以作为一个函数内部什么都没有则用pass填充（不加pass会报错）
#这里的while...else...即else语句在循环正常执行完的情况下执行（即不是通过break跳出循环的i情况下），for...else...也是一样
while num>10:
    print "while is start,num is",;print num
    num-=1
    if num ==15:
        print "while is break"
        break
    elif num<20:
        print "while is continue"
        continue
else:
    print "while is end,num is",;print num
'''
此循环会一直打印hello，但是可以使用ctrl+c来停止此循环
while True:
    print "hello"
'''
for letter in 'Python':#从Python字符串中一个一个字符输出
   print '当前字母 :', letter

fruits = ['banana', 'apple',  'mango']
for fruit in fruits:#从fruits列表中一个一个元素输出，迭代
   print '当前水果 :', fruit
for index in range(len(fruits)):#使用内置函数len（列表长度即元素个数）和range（返回序列数）获取索引遍历列表
    print '当前水果: ',fruits[index]
else:
    print "for end"

#math模块（属性运算函数）和cmath模块（复数运算函数），在使用前都必须先加import math
#abs\ceil\cmp\exp\fabs\floor\log\max\min\pow\round\sqrt\random\seed\choice\acos\asin\atan\sin\tan\radians\pi\e
import math
print dir(math)
print ;print ;
import cmath
print dir(cmath)
#字符串访问子字符串可用方括号来截取字符串，不支持单字符类型，在python中单字符也作为一个字符串使用
var='hello cd'
vara="welcome python world"
print var[0]#打印的为 h 字符
print var[7]+vara+' you are right'#字符串连接
#转义字符，反斜杠作为转义
#字符串运算符：+\-\*\[:]\in(成员运算)\not in\r(原始字符串，直接按字面意思来，没有转义或不能打印的字符)\R\%
#字符串格式化，和c中的printf函数语法一致，辅助指令*\<sp>\#\%
print "my name is %s and age is %d."%('zjj',30)
#字符串的三引号功能（单引号或双引号都可），允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符
he='''we are
the world
!'''
print he
#unicode字符串(这里会输出 hello world！)
print u'hello\u0020world!'
#字符串内建函数，string.capitalize\string.decode\string.encode\string.isalpha
#添加或删除列表项，+或*
print list
list.append("good gob")
print list
del list[5]
print list
list1=[1,2,3]
print list+list1
print list*2

#列表函数：comp\len(列表元素个数)\max\min\list(将元组转换成列表)\list.append\list.extend
#元组，与列表类似，只不过元素不能修改，元组使用小括号，列表使用方括号，元组虽然不能修改，但是可以对元素进行连接组合
#元组的元素值不允许删除，但是可以使用del语句删除整个元组
tup = ()#创建空元组
tup = (10,)#元组只包含一个元素时，需要在此元素后面添加逗号
tupadd = ("hello", ",","c")
print tup+tupadd
del tupadd#删除之后此元组不能再被使用，除非再次定义
print tup
#任意无符号的对象，以逗号隔开，默认为元组
print 'abc',"hello",4372
x,y=1,2
print "value of x,y: ",x,y

#字典是另一种可变容器模型，且可存储任意类型对象.字典的每个键值key=>value对用冒号:分割，每个键值对之间用逗号,分割，整个字典包括在花括号{}中,其中键一般是唯一的（若相同则后面的键会替换前面的键），值是可以取任意数据，访问字典里的值时只需把相应的键放入熟悉的方括号内即可
#键不可变，所以可以使用数字，字符串或元组充当，但不能用列表
d={'a':1,'b':2,'c':5,8:6}
print d
print d['b']
d['c']=3#更新键值
d['e']=4#添加字典内容
print d
del d['c']#删除单个键值对
print d
d.clear()#清空字典内容
print d
del d#删除字典

import time;#引入time模块
print time.time()#当前时间戳，总时间显示
print time.localtime(time.time())#time.struct_time(tm_year=2020, tm_mon=7, tm_mday=14, tm_hour=18, tm_min=9, tm_sec=0, tm_wday=1, tm_yday=196, tm_isdst=0),转换成年月日时分秒格式，其中tm_wday是0-6即0为周一，tm_isdst为是否是夏令时
print time.asctime(time.localtime(time.time()))#Tue Jul 14 18:09:00 2020
print time.strftime("%Y-%m-%d,%H:%M:%S",time.localtime())#时间转换成格式输出
print time.strftime("%a %b %d %H:%M:%S %Y",time.localtime())
a = "Sat Mar 28 22:24:24 2020"
print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))#将格式字符串转换为时间戳
import calendar#处理年历和月历
print calendar.month(2020,7)
print calendar.isleap(2020)
#其他处理日期和时间的模块：datetime、pytz、dateutil
#自定义函数：以def关键词开头，后接函数标识符名和圆括号()，函数内容以冒号起始并缩进，return结束函数
def func(arg1,arg2):
    "函数开始"
    print "function start......"
    total=arg1+arg2
    return total#退出函数，选择性地向调用方返回一个表达式。不带参数值的return语句返回None
print func(20,30)
#类型属于对象，变量是没有类型的，如：a=[1，2，3]，这里[]里面是list类型，而变量a是没有类型的，它仅仅是一个对象的引用(一个指针)
#可更改与不可更改对象：strings、tuples和numbers是不可更改的对象，而list和dict是可更改的对象，比如：a=10,a=20，实际是新生成一个int值对象20，再让a指向它，而10被丢弃，不是改变a的值，相当于新生成了a。可变类型：变量赋值la=[1,2,3,4]后再赋值la[2]=5则是将list la的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了
#函数的参数传递：不可变类型：类似 c++ 的值传递，如 整数、字符串、元组。如fun（a），传递的只是a的值，没有影响a对象本身。比如在 fun（a）内部修改a的值，只是修改另一个复制的对象，不会影响a本身。可变类型：类似c++的引用传递，如列表，字典。如fun（la），则是将la真正的传过去，修改后fun外部的la也会受影响
b=20
def changeinit(a):
    a=10
changeinit(b)
print b#其值是20而不会是10（实例中有int对象2，指向它的变量是b，在传递给ChangeInt函数时，按传值的方式复制了变量 b，a和b都指向了同一个Int对象，在a=10时，则新生成一个int值对象10，并让a指向它）

def changeme(mylist):
    mylist.append([1,2,3,4])
    #mylist=[1,2,3,4]
    print mylist#mylist.append输出的是[10, 20, 30, [1, 2, 3, 4]]，mylist=输出的是[1, 2, 3, 4]
mylist=[10,20,30]
changeme(mylist)
print mylist#mylist.append输出的是[10, 20, 30, [1, 2, 3, 4]]，mylist=输出的是[10, 20, 30]

#函数的参数
#可写函数说明，1.必备参数
def printme( str ):
   "打印任何传入的字符串"
   print str
   return
#调用printme函数
printme("hello,change.")
#printme()#报错

#可写函数说明，2.关键字参数
def printinfo( name, age ):
   "打印任何传入的字符串"
   print "Name: ", name
   print "Age ", age
   return
#调用printinfo函数
printinfo( age=50, name="miki" )

#可写函数说明，3.默认参数
def printinfo( name, age = 35 ):
   "打印任何传入的字符串"
   print "Name: ", name
   print "Age ", age
   return
#调用printinfo函数
printinfo( age=50, name="miki" )
printinfo( name="miki" )

"""
------函数的不定长参数------
def functionname([formal_args,] *var_args_tuple ):#加了星号（*）的变量名会存放所有未命名的变量参数
   "函数_文档字符串"
   function_suite
   return [expression]
"""
# 可写函数说明，4.不定长参数
def printinfo( arg1, *vartuple ):
   "打印任何传入的参数"
   print "输出: "
   print arg1
   for var in vartuple:
      print var
   return
# 调用printinfo 函数
printinfo( 10 )
printinfo( 70, 60, 50 )

"""
匿名函数：使用lambda来创建匿名函数
1.lambda只是一个表达式，函数体比def简单很多。
2.lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
3.lambda函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数。
4.虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率）
语法：lambda [arg1 [,arg2,.....argn]]:expression
"""
sum = lambda arg1, arg2: arg1 + arg2
# 调用sum函数
print "相加后的值为 : ", sum( 10, 20 )
print "相加后的值为 : ", sum( 20, 20 )

#变量作用域：全局变量和局部变量，和c语言差不多
"""
------Python 模块(Module)------
是一个 Python 文件，以 .py 结尾，包含了 Python 对象定义和Python语句。模块定义好后，我们可以使用 import 语句来引入模块，当解释器遇到import语句，若模块在当前搜索路径则会被导入，一个模块只会被导入一次
模块的语法：import module1[,module2......]，在调用模块内的函数时，引用：模块名.函数名
from modname import name1[,name2...]语句：从modname模块里的name1函数引入到执行这个声明的模块的全家符号表
from modname import* 语句：把模块的所有内容导入到当前命名空间，不能被过多使用
搜索路径：1当前目录；2在shell变量PYTHONPATH的每个目录；3查看默认路径，在unix下默认一般为/usr/local/lib/pthon/
"""
#PYTHONPATH 变量：环境变量
#set PYTHONPATH=c:\python27\lib;#windows下的环境变量
#et PYTHONPATH=/usr/local/lib/python#在unix下的环境变量
#如果要给函数内的全局变量赋值，必须使用 global 语句
print dir(math)# 函数一个排好序的字符串列表，内容是一个模块里定义过的名字
"""
如果在函数内部调用 locals()，返回的是所有能在该函数里访问的命名。

如果在函数内部调用 globals()，返回的是所有在该函数里能访问的全局名字。

两个函数的返回类型都是字典。所以名字们能用 keys() 函数摘取。

reload() 函数:当一个模块被导入到一个脚本，模块顶层部分的代码只会被执行一次。因此，如果你想重新执行模块里顶层部分的代码，可以用 reload() 函数。该函数会重新导入之前导入过的模块。语法为reload(modname),modname为模块的名字
"""
print dir(math)
#__init__.py 用于标识当前文件夹是一个包（ __init__.py 文件放在此文件夹里面）

"""
------文件I/O------
print语句：输出到屏幕
input/raw_input语句：读取键盘输入,input([prompt]) 函数和 raw_input([prompt]) 函数基本类似，但是 input 可以接收一个Python表达式作为输入，并将运算结果返回
open函数：打开文件，语法为file object = open(file_name [, access_mode][, buffering])
open之后的文件可使用与file对象相关的属性使用：object.closed是否关闭；object.name文件名称；object.mode访问模式
close：关闭文件。使用为【open的返回值.close，如前面的object.close】刷新缓冲区里任何还没写入的信息，并关闭该文件，这之后便不能再进行写入
write：写文件，object.write(string)
read：读文件，object.read(length)
tell：告诉你文件内的当前位置, 换句话说，下一次的读写会发生在文件开头这么多字节之后
seek（offset [,from]）：改变当前文件的位置。Offset变量表示要移动的字节数。From变量指定开始移动字节的参考位置
"""
"""
#若输入为：[x*5 for x in range(2,10,2)]
str=raw_input("please input: ")
print "input context is: ",str#结果是：[x*5 for x in range(2,10,2)]
str=input("please input: ")
print "input context is: ",str#结果是：[10, 20, 30, 40]
"""
#类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self
#使用点号 . 来访问对象的属性.
class Employee:
    '所有员工的基类'
    empCount = 0#类变量，可以在内部类或外部类使用 Employee.empCount 访问
 
    def __init__(self, name="bob", salary=5000):#类的构造函数或初始化方法，self 代表类的实例，self 在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数
        self.name = name
        self.salary = salary
        Employee.empCount += 1
   
    def displayCount(self):
        print "Total Employee %d" % Employee.empCount
 
    def displayEmployee(self):
        print "Name : ", self.name,  ", Salary: ", self.salary

    def __del__(self):#销毁函数
      class_name = self.__class__.__name__
      print class_name, "销毁"
      
t=Employee("bob","55$")
t.displayEmployee()
if hasattr(t,'displayEmployee'):#hasattr是判断t类中是否存在单引号的属性，这里是存在的
    print "this is class"
else:
    print "this isn't class"
print "Employee.__doc__:", Employee.__doc__#类的文档字符串
print "Employee.__name__:", Employee.__name__#类名
print "Employee.__module__:", Employee.__module__#类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
print "Employee.__bases__:", Employee.__bases__#类的所有父类构成元素（包含了一个由所有父类组成的元组）
print "Employee.__dict__:", Employee.__dict__#类的属性（包含一个字典，由类的数据属性组成）
class Child(Employee): # 定义子类
    def __init__(self):
        print "调用子类构造方法"
 
    def childMethod(self):
        print '调用子类方法'
c=Child()
c.childMethod()
c.displayCount()
del t
#运算符重载
class Vector:
    __secretCount = 0  # 私有变量,不能在类的外部调用,但可以使用 object._className__attrName（ 对象名._类名__私有属性名 ）访问属性
    publicCount = 0    # 公开变量
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def count(self):
        self.__secretCount+=1
        self.publicCount+=1
        print self.__secretCount
 
    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)
   
    def __add__(self,other):
        return Vector(self.a + other.a, self.b + other.b)
 
v1 = Vector(2,10)
print v1.publicCount
print v1._Vector__secretCount#访问私有属性
v2 = Vector(5,-2)
print v1 + v2

import socket
sockid=socket.socket(AF_INET,SOCK_STREAM,0)
