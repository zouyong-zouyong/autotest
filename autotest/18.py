import pymysql
'''
1.连接数据库
2.选择数据库 
3.获取游标
4.增删改查
'''

def query(sql):
    '''
    这是数据库的查询方法
    '''
    db   onnect(host="localhost",user="root",password="123456",db="sys") #选择并连接数据库
    cursor=db.cursor()   # 获取游标
    cursor.execute(sql)  # 执行SQL语句
    res=cursor.fetchall() #获得查询结果
    db.close()关闭数据库连接
    return res

aa=query("select * from tt_grade;")
print(aa[0][2])0