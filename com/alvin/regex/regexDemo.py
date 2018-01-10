# encoding: utf-8
import re

str = 'china is a very very good strong'
s1 = re.split(' ', str)
print('s1', s1)
print('-------------------')
for i in s1:
    print('i', i)
s2 = re.split('a', str)
print('s2', 2)

s3 = re.split('o', str)
print('s3', s3)

s4 = re.findall('\\bv.+?\\b', str)
print('s4', s4)

s5 = re.findall('\\bg.+?', str)
print('s5', s5)

s6 = re.split('\s', str)
for i in s6:
    print('i', i)

# re.compile('\\bg.+?\\b',str)

num = 'phone is 010-88888886666'
num1 = re.compile(r'(\d+)-(\d+)')
num2 = num1.search(num)
print(num2)
print(num2.group(1))
print('phone is', num2.group())

print(re.match('www', 'www.bdjw.com').span())
print(re.match('www', 'www.bdjw.com'))

pattern = re.compile(r'python')
match = pattern.match('hi python')
if match:
    print(match.group())
else:
    print(match)
