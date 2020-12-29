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
