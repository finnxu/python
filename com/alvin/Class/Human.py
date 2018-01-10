# encoding: utf-8
'''
    方法重载
'''


class human:
    name = ''
    __age = 0
    __phone = ''
    __sex = ''

    def __init__(self, age, phone, sex):
        self.__age = age
        self.__phone = phone
        self.__sex = sex

    def setName(self, name):
        self.name = name

    def show(self):
        print ('name:', self.name)
        print ('age:', self.__age)
        print ('phone:', self.__phone)
        print ('sex:', self.__sex)
