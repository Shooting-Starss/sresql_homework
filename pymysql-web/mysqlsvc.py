import pymysql
from flask import Flask,request
from gevent import pywsgi

#定义mysql操作对象
conn = pymysql.connect(
    host="43.143.129.174",  # 数据库的ip地址
    port=3306,  # 数据库的端口号
    user="root",  # 登陆数据库的用户名
    passwd="197874",  # 登陆数据库的密码
    db="sre_user"  # 要连接的数据库，必须提前创建好，否则会连接出错
)
cursor = conn.cursor()
cursor.execute("show tables")

app = Flask(__name__)

#实现注册用户的功能
@app.post('/register')
def register():
    account_num = request.args.get("account_num", "")
    account_name = request.args.get("account_name", "")
    account_pass = request.args.get("account_pass", "")
    # question = request.args.get("question", "")
    # question_content = request.args.get("question_content", "")
    entry_date = request.args.get("entry_date", "")
    info = (account_num, account_name, account_pass,entry_date)
    try:
        cursor.execute("insert into users (account_num,account_name,account_pass,entry_date) value(%s,%s,%s,%s)", info)
        conn.commit()
        return "注册成功，你的用户名是" + account_name
    except Exception as e:
        print(e)
        return "注册出错了捏"

@app.get('/get_info')
def get_info():
    account_name = request.args.get("account_name", "")
    cursor.execute("select * from users where account_name=%s", account_name)
    conn.commit()
    result = cursor.fetchone()
    print(list(result))
    return {"data": list(result)}


if __name__ == '__main__':
    print(app.url_map)
    app.run(host='0.0.0.0', port=5000)