from flask import request, session
from flask import Flask
import mysql.connector
app = Flask( __name__, static_folder='D:/workspace/workspace2/')
app.config['SECRET_KEY'] = 'dasdefaf9*&*Tfdad'
conn = mysql.connector.connect(host='127.0.0.1', user='bbt',
                               passwd='bbtbbtbbt', database='bbt_demo',
                               charset='utf8mb4')
db = conn.cursor()
@app.route('/bbt/regist', methods=['POST'])
def register():
    # 在此我们使用了restful风格, 可以看到甚至不需要告诉你这是一个什么接口

    data = request.get_json()  # 在content-type=application/json时, 可以通过该方法获取数据
    username = data['username']
    password = data['password']
    print('=================')
    print(username, password)
    db.execute('select `username` from users where `username`=%s', (username,))

    result = db.fetchall()

    if result:
        return {
            'errcode': 400,
            'errmsg': '该用户名已被注册'
        }, 400

    db.execute(
        'insert into users (`username`, `password`) values (%s, %s)', (username, password))
    if db.rowcount > 0:  # rowcount为影响数据数目, 成功插入即影响一条数据, 同理update, delete
        return {
            'errcode': 0,
            'errmsg': '注册成功'
        }, 200

    return {
        'errcode': 400,
        'errmsg': '出现错误'
    }, 400


from login import *


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9990)  # 将运行在本地回路ip的9990端口
