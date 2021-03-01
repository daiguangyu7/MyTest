# python连接并且查询mysql数据库

import pymysql

# 数据库连接信息
DBCONFIG = {
    "host": "118.24.255.132",
    "port": 3306,
    "user": "testgoup",
    "password":"1qaz!QAZ",
    "db": "ljtestdb"
}

def query(sql):
    """
        方法：python连接并且查询数据库
        参数：sql："select * from t_user where xxxx"
        返回值：
            ((id, username, password, ...), (id2, username2, password2...))
    """
    # 步骤1：连接并且打开对应的数据库
    db = pymysql.connect(host=DBCONFIG["host"], port=DBCONFIG["port"], user=DBCONFIG["user"], password=DBCONFIG["password"], db=DBCONFIG["db"])
    # 步骤2：获取查询的窗口：游标
    cur = db.cursor()
    # 步骤3：执行sql语句
    cur.execute(sql)
    # 步骤4：获取对应的结果
    res = cur.fetchall()
    # 步骤5：关闭数据库
    db.close()
    
    return res


# 从外部导入这个dbtools的时候，不要运行测试代码
if __name__ == "__main__":
    sql = "select * from t_user where username ='liuyun2'"
    r = query(sql)
    print(r)