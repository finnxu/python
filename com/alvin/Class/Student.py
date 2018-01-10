# encoding: utf-8
from com.alvin.Class.Human import human

'''
    方法重载
'''


class student(human):
    __classess = ''
    __grade = ''
    __num = 0

    def __init__(self, classess, grade, num, age, phone, sex):
        self.__classess = classess
        self.__grade = grade
        self.__num = num
        human.__init__(self, age, phone, sex)

    def show(self):
        human.show(self)
        print ('classess:', self.__classess)
        print ('grade:', self.__grade)
        print ('num:', self.__num)
