# encoding: utf-8
def hi():
    print('hi python')


# 求和函数
def listSum(L):
    result = 0
    for i in L:
        result = result + i
    return result


# 打印函数
def printAll(X):
    for i in X:
        print(i)


def cube1(x=5):
    return x ** 3


def cube3(x=1, y=1, z=1):
    return x + y - z


def cube4(x, y, z):
    return x + y - z


def cubeNone(x=None, y=None, z=None):
    if x == None:
        x = 10
    if y == None:
        y = 10
    if z == None:
        z = 10
    return x + y - z


def listAppand(*list):
    l = []
    for i in list:
        l.extend(i)
    return l


def show():
    print('lambda')


def show(n):
    print('lambda' * n)


if __name__ == '__main__':
    # hi()
    # l = [1, 2, 3, 4]
    # printAll(l)
    # t = ('a', 'c', 'd')
    # printAll(t)
    # print listSum(l)
    # print cube1(2)
    # print cube1()
    # print cube3(2, 3, 4)
    # print cube3(10, 10)
    # print cube4(1, 2, 3)
    # print cube4(x=10, y=10, z=10)
    # print cubeNone(None, None, 100)
    # a = [1, 2, 3]
    # b = [4, 5, 6]
    # c = [7, 8, 9]
    # d = ['a', 'b']
    # e = ['c', 'd']
    # print listAppand(a, b, c)
    # print listAppand(d, e)
    # f = lambda: show()
    # f()
    fn = lambda x: show(x)
    fn(4)
