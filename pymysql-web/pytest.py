import pymysql

#定义mysql操作对象
conn = pymysql.connect(
    host="43.143.129.174",  # 数据库的ip地址
    port=3306,  # 数据库的端口号
    user="root",  # 登陆数据库的用户名
    passwd="197874",  # 登陆数据库的密码
    db="sre_user"  # 要连接的数据库，必须提前创建好，否则会连接出错
)
#定义光标，我们通过这个光标执行sql语句
cursor = conn.cursor()
cursor.execute("show tables")
info = (202245678,"iloveutooo",1010102333,"2023-1-4")
#执行插入语句
#使用下面的句子，如果是面向外部的接口，就容易被sql注入
# cursor.execute("insert into user (id,username,password,question,question_content) value(%s,'%s','%s','%s','%s')"%info)
#使用pymysql提供的参数化语句避免sql注入，用法如下
#对比发现，使用参数化语句还有一个好处是，不用去管数据的类型了，pymysql会帮你处理
# cursor.execute("insert into users (account_num,account_name,account_pass,entry_date) value(%s,%s,%s,%s)", info)
# conn.commit()
#执行查表语句
cursor.execute("select * from users where account_name=%s", "iloveutoo")
conn.commit()
result = cursor.fetchone()
print(result)
conn.close()