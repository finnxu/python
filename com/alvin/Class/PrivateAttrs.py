# encoding: utf-8
class Person:
    __name = ''
    __age = 0
    _phone = ''

    def show(self):
        print ('name:',self.__name)
        print ('age:',self.__age)
        print ('phone:',self._phone)

    def setName(self,name):
        self.__name = name

    def getName(self,name):
        return name

    def setAge(self,age):
        self.__age = age

    def setPhone(self,phone):
        self._phone = phone
