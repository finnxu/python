# encoding: utf-8
from com.alvin.Class.ClassDemo import book
from com.alvin.Class.PrivateAttrs import Person
from com.alvin.Class.Student import student

if __name__ == '__main__':
    print ('------book--------')
    a = book()
    b = book()
    a.author = 'alvin'
    a.name = '征服python'
    a.pages = 1000
    a.price = 66.6
    print ('author :',a.author)
    print ('name :',a.name)
    print ('pages :',a.pages)
    print ('price :',a.price)

    print ('---------book----------')

    b.author = 'alvin';
    b.name = '征服spark'
    b.pages = 1000000
    b.price = 100.00
    print ('author :',b.author)
    print ('name :',b.name)
    print ('pages :',b.pages)
    print ('price :',b.price)

    print ('---------person-------------')

    person = Person();
    person.setName('alvin')
    person.setAge(18)
    person.setPhone('11111111111')
    person.show()

    print ('---------student--------------')
    stu = student('17级','2班',100,22,'153****7286','男')
    stu.setName('alvin')
    stu.show()
