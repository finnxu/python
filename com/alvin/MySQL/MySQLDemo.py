import pymysql

try:
    # 获取连接
    connect = pymysql.connect(
        host='localhost',
        port=56361,
        user='root',
        passwd='root',
        db='python',
        charset='utf8'
    )

    cursor = connect.cursor()

    # 创建表
    # sql = 'create table person(name varchar(30),age int,sex char(1))'
    # cursor.execute(sql)
    # 插入数据
    sql = 'insert into person values("alvin",22,"M")'
    try:
        cursor.execute(sql)
        connect.commit()
    except:
        connect.rollback()
    # 查询数据
    sql = 'select * from person'
    cursor.execute(sql)
    data = cursor.fetchall()
    for i in data:
        print('name:', str(i[0]), 'age:', str(i[1]), 'sex:', str(i[2]))
    cursor.close()
    connect.close()
except Exception:
    print('发生不可知异常错误')
