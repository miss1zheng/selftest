'''
#!/usr/bin/python
# -*- coding:utf-8 -*-
#ǰ������һ���Ǽ��ر�������һ���Ǽ��ر����ʽ
'''
print ("hello,world.����"),#printĬ���ǻ��еģ������ں����һ�����žͱ�ʾ���ỻ��
okif="if is ok." + \
      "add string"#+Ϊ���������ַ���
okdan=['add','b','class','del','else','if',
           'g','h','item','j','k','l','m','num']
oknum,errnum,endstr,complex_num,longnum=11,22.2,"end",9.34e-36j,0122L#����Ϊ��ֵ���ͣ������ͣ��ַ����������ͣ��������һ����������
okvalue = errvalue = 1;#�������ֵ

if True:
    print okif[1:14]*2  #�±��0��ʼ��ð�ź���Ϊ��ȡ������������������"f is o"������*2��ʾ������Σ������"f is of is o"
    print okdan[0]      #ֻ������±��ַ���
    print okdan[3:]     #�±꿪ʼ�����ȫ�����
    print oknum*2       #��11*2=22
    print okdan[2:9:4]  #��ȡ�ַ���������ʼһ�����±�Ϊ2���ַ�����Ȼ�����һ��Ϊ[9-(4+2)]=4�������±�Ϊ9��ʼ��ǰ�ƶ��ĸ�λ�õ��ַ���
    print okdan[-6]     #��ȡ������6��Ԫ��
else:
    print errnum;print("else is end.")
print endstr

#ɾ��һЩ���������
#print oknum#ɾ����֮��Ͳ�����ʹ����
del oknum
del errnum,endstr

raw_input("we are used to \"enter\" funtion.")#�˺�������Ϊ������"enter"���Ż�ִ����������

print "";print "�б�";print ""
"""
�б�
"""
list=["111","aaa",111,'bbb','222']
otherlist=['hhh',999]
print list
print list[0]
print list[2:]
print list[1:4]
print list*2
print list+otherlist

print "";print "Ԫ��";print ""
'''
Ԫ��
'''
list=("111","aaa",111,'bbb','222')
otherlist=('hhh',999)
print list
print list[0]
print list[2:]
print list[1:4]
print list*2
print list+otherlist


print "";print "�ֵ�";print ""
"""
�ֵ�(dictionary)�ǳ��б�����python֮���������������ݽṹ���͡��б�������Ķ��󼯺ϣ��ֵ�������Ķ��󼯺ϡ�

����֮����������ڣ��ֵ䵱�е�Ԫ����ͨ��������ȡ�ģ�������ͨ��ƫ�ƴ�ȡ.
�ֵ���"{ }"��ʶ���ֵ�������(key)������Ӧ��ֵvalue���.
"""
dict={}
dict['one']="this is one"
dict[2]="this is two"
tinydict = {'name':'john','code':7654,'dept':'sales'}
print dict['one']          # �����Ϊ'one' ��ֵ
print dict[2]              # �����Ϊ 2 ��ֵ
print tinydict             # ����������ֵ�
print tinydict.keys()      # ������м�
print tinydict.values()    # �������ֵ

'''
��������ת��
'''
int('a',16)     #ʮ�����ƣ�ֵΪ��10
int('0x0a',16)  #ֵΪ��10
int()           #ʮ���ƣ�ֵΪ��0
int(3)          #ֵΪ��3
int(5.8)        #ֵΪ��5.8
int('10',8)     #�˽���ֵΪ��8

long()          #ֵΪ��0L
long(3)         #ֵΪ��3L
long('123')     #ֵΪ��123L

float()         #ֵΪ��0.0
float(134)      #ֵΪ��134.0
float(-134.5)   #ֵΪ��-134.5
float('134')    #ֵΪ��134.0
#����
complex()       #ֵΪ��0j
complex(2,3)    #ֵΪ��(2+3j)
complex("1")    #ֵΪ��(1+0j)
complex("1+2j") #ֵΪ��(1+2j)
#�ַ���
str()           #ֵΪ��''
str('runoob')   #ֵΪ��'runoob'
#���ʽ�ַ���
repr('runoob')   #ֵΪ��"'runoob'"
#eval('3*9')
#eval('pow(2,2)')
#tuple([1,2,3,4])
#tuple([1:2,3:4])#�ֵ�
#list();set();dict();frozenset();chr();unichr();ord();hex();oct()
#��������
print (30-10)*20/10%20#30-10=20x20=400/10=40%20=0
print 20**2//24#400/24=16(ʵ����Ϊ16.5����Ҫ����)����������**��ʾȡ�ݣ�//��ʾȡ��������������
#�Ƚ�����
print 1==1#����True
print 1!=1
print 1>2
print 1<2
print 1<=2
#��ֵ����
a=10;b=20;b+=a;b-=a;b*=a;b/=a;b%=a;b**=a;b//=a
#λ����
a=60;b=13
print a&b
print a|b
print a^b
print ~a
print a<<4
print b<<4
#�߼�����
a=10;b=20
print (a and b)
print (a or b)
print not(a and b)
#��Ա���㣨�磺�ж�a�Ƿ���b�б��У���in��Ԫ���Ƿ�����б���
list=["111","aaa",111,'bbb','222']
if(111 in list):
    print '111 in list.'
elif("111" in list):
    print '111 str in list'
elif("bbb" not in list):
    print "bbb not in list"
else:
    print "haven't this value"
#�������(is �� == ���������ж������������ö����Ƿ�Ϊͬһ��(ͬһ���ڴ�ռ�)�� == �����ж����ñ�����ֵ�Ƿ����)
a=10;b=20
if(a is b):
    print "����ͬһ������"
elif(a is not b):
    print "���Բ�ͬ����"
#��������ȼ�
#������䣨�κη�0��ǿ�null����ֵΪTure��Ϊ0��յ�ֵΪFalse
num=30
if (num<0 or num>20):
    print "num about over20 or less than 0"
elif(num>0 and num < 5) or (num>10 and num <20):
    print "num about 0-5 or 10-20"
    if(num>0 and num < 5):
        print "num value is 0-5"
    elif(num>10 and num <20):
        print "num value is 10-20"
#ѭ����䣺for��while(�κη�0��ǿ�null����ֵΪTure����Ϊfalseʱѭ������)
#break �˳��ڲ�ѭ����continue ���������ô�ѭ��(���¿�ʼ�ڲ�ѭ��)
#passʱ����䲻���κ����飬ֻ��Ϊ�˱��ֳ���ṹ�������ԣ�һ������ռλ��䣬Ҳ������Ϊһ�������ڲ�ʲô��û������pass��䣨����pass�ᱨ��
#�����while...else...��else�����ѭ������ִ����������ִ�У�������ͨ��break����ѭ����i����£���for...else...Ҳ��һ��
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
��ѭ����һֱ��ӡhello�����ǿ���ʹ��ctrl+c��ֹͣ��ѭ��
while True:
    print "hello"
'''
for letter in 'Python':#��Python�ַ�����һ��һ���ַ����
   print '��ǰ��ĸ :', letter

fruits = ['banana', 'apple',  'mango']
for fruit in fruits:#��fruits�б���һ��һ��Ԫ�����������
   print '��ǰˮ�� :', fruit
for index in range(len(fruits)):#ʹ�����ú���len���б��ȼ�Ԫ�ظ�������range����������������ȡ���������б�
    print '��ǰˮ��: ',fruits[index]
else:
    print "for end"

#mathģ�飨�������㺯������cmathģ�飨�������㺯��������ʹ��ǰ�������ȼ�import math
#abs\ceil\cmp\exp\fabs\floor\log\max\min\pow\round\sqrt\random\seed\choice\acos\asin\atan\sin\tan\radians\pi\e
import math
print dir(math)
print ;print ;
import cmath
print dir(cmath)
#�ַ����������ַ������÷���������ȡ�ַ�������֧�ֵ��ַ����ͣ���python�е��ַ�Ҳ��Ϊһ���ַ���ʹ��
var='hello cd'
vara="welcome python world"
print var[0]#��ӡ��Ϊ h �ַ�
print var[7]+vara+' you are right'#�ַ�������
#ת���ַ�����б����Ϊת��
#�ַ����������+\-\*\[:]\in(��Ա����)\not in\r(ԭʼ�ַ�����ֱ�Ӱ�������˼����û��ת����ܴ�ӡ���ַ�)\R\%
#�ַ�����ʽ������c�е�printf�����﷨һ�£�����ָ��*\<sp>\#\%
print "my name is %s and age is %d."%('zjj',30)
#�ַ����������Ź��ܣ������Ż�˫���Ŷ��ɣ�������һ���ַ�������У��ַ����п��԰������з����Ʊ���Լ����������ַ�
he='''we are
the world
!'''
print he
#unicode�ַ���(�������� hello world��)
print u'hello\u0020world!'
#�ַ����ڽ�������string.capitalize\string.decode\string.encode\string.isalpha
#��ӻ�ɾ���б��+��*
print list
list.append("good gob")
print list
del list[5]
print list
list1=[1,2,3]
print list+list1
print list*2

#�б�����comp\len(�б�Ԫ�ظ���)\max\min\list(��Ԫ��ת�����б�)\list.append\list.extend
#Ԫ�飬���б����ƣ�ֻ����Ԫ�ز����޸ģ�Ԫ��ʹ��С���ţ��б�ʹ�÷����ţ�Ԫ����Ȼ�����޸ģ����ǿ��Զ�Ԫ�ؽ����������
#Ԫ���Ԫ��ֵ������ɾ�������ǿ���ʹ��del���ɾ������Ԫ��
tup = ()#������Ԫ��
tup = (10,)#Ԫ��ֻ����һ��Ԫ��ʱ����Ҫ�ڴ�Ԫ�غ�����Ӷ���
tupadd = ("hello", ",","c")
print tup+tupadd
del tupadd#ɾ��֮���Ԫ�鲻���ٱ�ʹ�ã������ٴζ���
print tup
#�����޷��ŵĶ����Զ��Ÿ�����Ĭ��ΪԪ��
print 'abc',"hello",4372
x,y=1,2
print "value of x,y: ",x,y

#�ֵ�����һ�ֿɱ�����ģ�ͣ��ҿɴ洢�������Ͷ���.�ֵ��ÿ����ֵkey=>value����ð��:�ָÿ����ֵ��֮���ö���,�ָ�����ֵ�����ڻ�����{}��,���м�һ����Ψһ�ģ�����ͬ�����ļ����滻ǰ��ļ�����ֵ�ǿ���ȡ�������ݣ������ֵ����ֵʱֻ�����Ӧ�ļ�������Ϥ�ķ������ڼ���
#�����ɱ䣬���Կ���ʹ�����֣��ַ�����Ԫ��䵱�����������б�
d={'a':1,'b':2,'c':5,8:6}
print d
print d['b']
d['c']=3#���¼�ֵ
d['e']=4#����ֵ�����
print d
del d['c']#ɾ��������ֵ��
print d
d.clear()#����ֵ�����
print d
del d#ɾ���ֵ�

import time;#����timeģ��
print time.time()#��ǰʱ�������ʱ����ʾ
print time.localtime(time.time())#time.struct_time(tm_year=2020, tm_mon=7, tm_mday=14, tm_hour=18, tm_min=9, tm_sec=0, tm_wday=1, tm_yday=196, tm_isdst=0),ת����������ʱ�����ʽ������tm_wday��0-6��0Ϊ��һ��tm_isdstΪ�Ƿ�������ʱ
print time.asctime(time.localtime(time.time()))#Tue Jul 14 18:09:00 2020
print time.strftime("%Y-%m-%d,%H:%M:%S",time.localtime())#ʱ��ת���ɸ�ʽ���
print time.strftime("%a %b %d %H:%M:%S %Y",time.localtime())
a = "Sat Mar 28 22:24:24 2020"
print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))#����ʽ�ַ���ת��Ϊʱ���
import calendar#��������������
print calendar.month(2020,7)
print calendar.isleap(2020)
#�����������ں�ʱ���ģ�飺datetime��pytz��dateutil
#�Զ��庯������def�ؼ��ʿ�ͷ����Ӻ�����ʶ������Բ����()������������ð����ʼ��������return��������
def func(arg1,arg2):
    "������ʼ"
    print "function start......"
    total=arg1+arg2
    return total#�˳�������ѡ���Ե�����÷�����һ�����ʽ����������ֵ��return��䷵��None
print func(20,30)
#�������ڶ��󣬱�����û�����͵ģ��磺a=[1��2��3]������[]������list���ͣ�������a��û�����͵ģ���������һ�����������(һ��ָ��)
#�ɸ����벻�ɸ��Ķ���strings��tuples��numbers�ǲ��ɸ��ĵĶ��󣬶�list��dict�ǿɸ��ĵĶ��󣬱��磺a=10,a=20��ʵ����������һ��intֵ����20������aָ��������10�����������Ǹı�a��ֵ���൱����������a���ɱ����ͣ�������ֵla=[1,2,3,4]���ٸ�ֵla[2]=5���ǽ�list la�ĵ�����Ԫ��ֵ���ģ�����laû�ж���ֻ�����ڲ���һ����ֵ���޸���
#�����Ĳ������ݣ����ɱ����ͣ����� c++ ��ֵ���ݣ��� �������ַ�����Ԫ�顣��fun��a�������ݵ�ֻ��a��ֵ��û��Ӱ��a������������ fun��a���ڲ��޸�a��ֵ��ֻ���޸���һ�����ƵĶ��󣬲���Ӱ��a�����ɱ����ͣ�����c++�����ô��ݣ����б��ֵ䡣��fun��la�������ǽ�la�����Ĵ���ȥ���޸ĺ�fun�ⲿ��laҲ����Ӱ��
b=20
def changeinit(a):
    a=10
changeinit(b)
print b#��ֵ��20��������10��ʵ������int����2��ָ�����ı�����b���ڴ��ݸ�ChangeInt����ʱ������ֵ�ķ�ʽ�����˱��� b��a��b��ָ����ͬһ��Int������a=10ʱ����������һ��intֵ����10������aָ������

def changeme(mylist):
    mylist.append([1,2,3,4])
    #mylist=[1,2,3,4]
    print mylist#mylist.append�������[10, 20, 30, [1, 2, 3, 4]]��mylist=�������[1, 2, 3, 4]
mylist=[10,20,30]
changeme(mylist)
print mylist#mylist.append�������[10, 20, 30, [1, 2, 3, 4]]��mylist=�������[10, 20, 30]

#�����Ĳ���
#��д����˵����1.�ر�����
def printme( str ):
   "��ӡ�κδ�����ַ���"
   print str
   return
#����printme����
printme("hello,change.")
#printme()#����

#��д����˵����2.�ؼ��ֲ���
def printinfo( name, age ):
   "��ӡ�κδ�����ַ���"
   print "Name: ", name
   print "Age ", age
   return
#����printinfo����
printinfo( age=50, name="miki" )

#��д����˵����3.Ĭ�ϲ���
def printinfo( name, age = 35 ):
   "��ӡ�κδ�����ַ���"
   print "Name: ", name
   print "Age ", age
   return
#����printinfo����
printinfo( age=50, name="miki" )
printinfo( name="miki" )

"""
------�����Ĳ���������------
def functionname([formal_args,] *var_args_tuple ):#�����Ǻţ�*���ı�������������δ�����ı�������
   "����_�ĵ��ַ���"
   function_suite
   return [expression]
"""
# ��д����˵����4.����������
def printinfo( arg1, *vartuple ):
   "��ӡ�κδ���Ĳ���"
   print "���: "
   print arg1
   for var in vartuple:
      print var
   return
# ����printinfo ����
printinfo( 10 )
printinfo( 70, 60, 50 )

"""
����������ʹ��lambda��������������
1.lambdaֻ��һ�����ʽ���������def�򵥺ܶࡣ
2.lambda��������һ�����ʽ��������һ������顣��������lambda���ʽ�з�װ���޵��߼���ȥ��
3.lambda����ӵ���Լ��������ռ䣬�Ҳ��ܷ������в����б�֮���ȫ�������ռ���Ĳ�����
4.��Ȼlambda����������ֻ��дһ�У�ȴ����ͬ��C��C++���������������ߵ�Ŀ���ǵ���С����ʱ��ռ��ջ�ڴ�Ӷ���������Ч�ʣ�
�﷨��lambda [arg1 [,arg2,.....argn]]:expression
"""
sum = lambda arg1, arg2: arg1 + arg2
# ����sum����
print "��Ӻ��ֵΪ : ", sum( 10, 20 )
print "��Ӻ��ֵΪ : ", sum( 20, 20 )

#����������ȫ�ֱ����;ֲ���������c���Բ��
"""
------Python ģ��(Module)------
��һ�� Python �ļ����� .py ��β�������� Python �������Python��䡣ģ�鶨��ú����ǿ���ʹ�� import ���������ģ�飬������������import��䣬��ģ���ڵ�ǰ����·����ᱻ���룬һ��ģ��ֻ�ᱻ����һ��
ģ����﷨��import module1[,module2......]���ڵ���ģ���ڵĺ���ʱ�����ã�ģ����.������
from modname import name1[,name2...]��䣺��modnameģ�����name1�������뵽ִ�����������ģ���ȫ�ҷ��ű�
from modname import* ��䣺��ģ����������ݵ��뵽��ǰ�����ռ䣬���ܱ�����ʹ��
����·����1��ǰĿ¼��2��shell����PYTHONPATH��ÿ��Ŀ¼��3�鿴Ĭ��·������unix��Ĭ��һ��Ϊ/usr/local/lib/pthon/
"""
#PYTHONPATH ��������������
#set PYTHONPATH=c:\python27\lib;#windows�µĻ�������
#et PYTHONPATH=/usr/local/lib/python#��unix�µĻ�������
#���Ҫ�������ڵ�ȫ�ֱ�����ֵ������ʹ�� global ���
print dir(math)# ����һ���ź�����ַ����б�������һ��ģ���ﶨ���������
"""
����ں����ڲ����� locals()�����ص����������ڸú�������ʵ�������

����ں����ڲ����� globals()�����ص��������ڸú������ܷ��ʵ�ȫ�����֡�

���������ķ������Ͷ����ֵ䡣�������������� keys() ����ժȡ��

reload() ����:��һ��ģ�鱻���뵽һ���ű���ģ�鶥�㲿�ֵĴ���ֻ�ᱻִ��һ�Ρ���ˣ������������ִ��ģ���ﶥ�㲿�ֵĴ��룬������ reload() �������ú��������µ���֮ǰ�������ģ�顣�﷨Ϊreload(modname),modnameΪģ�������
"""
print dir(math)
#__init__.py ���ڱ�ʶ��ǰ�ļ�����һ������ __init__.py �ļ����ڴ��ļ������棩

"""
------�ļ�I/O------
print��䣺�������Ļ
input/raw_input��䣺��ȡ��������,input([prompt]) ������ raw_input([prompt]) �����������ƣ����� input ���Խ���һ��Python���ʽ��Ϊ���룬��������������
open���������ļ����﷨Ϊfile object = open(file_name [, access_mode][, buffering])
open֮����ļ���ʹ����file������ص�����ʹ�ã�object.closed�Ƿ�رգ�object.name�ļ����ƣ�object.mode����ģʽ
close���ر��ļ���ʹ��Ϊ��open�ķ���ֵ.close����ǰ���object.close��ˢ�»��������κλ�ûд�����Ϣ�����رո��ļ�����֮��㲻���ٽ���д��
write��д�ļ���object.write(string)
read�����ļ���object.read(length)
tell���������ļ��ڵĵ�ǰλ��, ���仰˵����һ�εĶ�д�ᷢ�����ļ���ͷ��ô���ֽ�֮��
seek��offset [,from]�����ı䵱ǰ�ļ���λ�á�Offset������ʾҪ�ƶ����ֽ�����From����ָ����ʼ�ƶ��ֽڵĲο�λ��
"""
"""
#������Ϊ��[x*5 for x in range(2,10,2)]
str=raw_input("please input: ")
print "input context is: ",str#����ǣ�[x*5 for x in range(2,10,2)]
str=input("please input: ")
print "input context is: ",str#����ǣ�[10, 20, 30, 40]
"""
#��ķ�������ͨ�ĺ���ֻ��һ���ر�����𡪡����Ǳ�����һ������ĵ�һ����������, ���չ������������� self
#ʹ�õ�� . �����ʶ��������.
class Employee:
    '����Ա���Ļ���'
    empCount = 0#��������������ڲ�����ⲿ��ʹ�� Employee.empCount ����
 
    def __init__(self, name="bob", salary=5000):#��Ĺ��캯�����ʼ��������self �������ʵ����self �ڶ�����ķ���ʱ�Ǳ����еģ���Ȼ�ڵ���ʱ���ش�����Ӧ�Ĳ���
        self.name = name
        self.salary = salary
        Employee.empCount += 1
   
    def displayCount(self):
        print "Total Employee %d" % Employee.empCount
 
    def displayEmployee(self):
        print "Name : ", self.name,  ", Salary: ", self.salary

    def __del__(self):#���ٺ���
      class_name = self.__class__.__name__
      print class_name, "����"
      
t=Employee("bob","55$")
t.displayEmployee()
if hasattr(t,'displayEmployee'):#hasattr���ж�t�����Ƿ���ڵ����ŵ����ԣ������Ǵ��ڵ�
    print "this is class"
else:
    print "this isn't class"
print "Employee.__doc__:", Employee.__doc__#����ĵ��ַ���
print "Employee.__name__:", Employee.__name__#����
print "Employee.__module__:", Employee.__module__#�ඨ�����ڵ�ģ�飨���ȫ����'__main__.className'�������λ��һ������ģ��mymod�У���ôclassName.__module__ ���� mymod��
print "Employee.__bases__:", Employee.__bases__#������и��๹��Ԫ�أ�������һ�������и�����ɵ�Ԫ�飩
print "Employee.__dict__:", Employee.__dict__#������ԣ�����һ���ֵ䣬���������������ɣ�
class Child(Employee): # ��������
    def __init__(self):
        print "�������๹�췽��"
 
    def childMethod(self):
        print '�������෽��'
c=Child()
c.childMethod()
c.displayCount()
del t
#���������
class Vector:
    __secretCount = 0  # ˽�б���,����������ⲿ����,������ʹ�� object._className__attrName�� ������._����__˽�������� ����������
    publicCount = 0    # ��������
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
print v1._Vector__secretCount#����˽������
v2 = Vector(5,-2)
print v1 + v2

import socket
sockid=socket.socket(AF_INET,SOCK_STREAM,0)
