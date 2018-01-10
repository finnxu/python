# -*- coding: utf-8 -*-
a = 10
b = 20
"""
if a > b:
    print("a>b")
else:
    print("a<b")
if a > b:
    if a == 1:
        print 1
    else:
        if a == 0:
            print 0
        else:
            pass
elif a == b:
    print a * b
else:
    print b - a
name = raw_input("what's your name:")
print(name)
age = raw_input("what's your age:")
print(age)
print(int(age)+1)
l = [1,2,3,4]
print(l)
t = ["a","b","c"]
print(t)
print l,t
for i in t :
    print(i)
a = 10
b = 10.10
c = a + b
print(c)
d = 1111111111111111111111111111111111111111111111111111111111111111111111111111111
print(d)
str1 = '这是单引号'
print(str1)
str2 = "这是双引号"
print(str2)
str3 = "这个是‘混\r合引号"
print(str3)
str = "akdhfjHdjvhbYhdghdsgfhd"
print(str.capitalize())
print(str.count("d"))
print(str.decode("utf-8"))
print(str.encode("GBK"))
print(str.find("d"))
print(str.isalnum())
print(str.isalpha())
print(str.isdigit())
print(str.islower())
print(str.isupper())
print(str.istitle())
print(str.isspace())
print(str.join("11"))
print(str.upper())
print(str.split("d"))
print(str.swapcase())
print(len(str))
print str[2]
print str[-2]
print str[2:4]
print str[0:-1]
import string
str = '10' + str(4)
print str
a = '10'
b = string.atoi(a) + 4
print b
print(string.atoi('15',10))
print(string.atoi('15',8))
原始字符串
列表
list = []
print list
list.append(1)
print(list)
list.extend([10,3,2,5,1])
print list
print(list.index(3))
list.insert(1,10)
print(list)
list.pop(1)
print list
list.reverse()
print list
list.sort()
print list
tuple = ('a','d','v')
print tuple
list.insert(3,tuple)
print list
print list[3]
print list[1:5]
print tuple[1:2]
字典
dic = {'china': 100, 'us': 2}
print dic
print(dic.copy())
dic['USA'] = 10
print(dic)
print(dic.items())
#dic.pop('ua')
#print(dic)
print dic.keys()
print dic.values()
dic.update({'china':1000000000000})
print(dic)
dic.update({"qqqq":11})
print dic
print dic['qqqq']
dic.clear()
print dic
文件
path = open('D:/python/Project/com/alvin/study/test.py','r')
re = path.read()
print re
path.close()
python基本语句
if语句
if a == b:
    print "a==b"
elif a > b:
    print "a>b"
else:
    print "a<b"
m = 'hi'
n = 'hello'
if m == n:
    print True
elif m < n:
    print False
else:
    print m,n
for语句
for i in [1, 2, 3, 4, 5, 6]:
    if i == 7:
        break
    elif i % 2 == 0:
        print i
    else:
        print 'all'
for i in range(1, 10 + 1):
    print i
dic = {'china': 100, 'us': 2}
for d in dic:
    print d
    print dic[d]
tt = (('q','z'),('y','r'),('m','u'),('d','w'),('q','g'))
for t in tt:
    print t
for (x,y) in tt:
    print x,y
#求解50到100之间的素数
import math
for i in range(50,100+1):
    for t in range(2,int(math.sqrt(i))+1):
        if i % t == 0:
            break
    else:
        print i
"""
#while语句
x = 1
while x < 6:
    print (x)
    x = x +1