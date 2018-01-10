# encoding: utf-8
class Except:
    l = [1, 2, 3, 4]
    try:
        l[2] / 0
    except IndexError:
        print ('列表下标越界')
    except ZeroDivisionError:
        print ('除数不能为0')
    else:
        print ('no error')
