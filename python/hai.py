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
