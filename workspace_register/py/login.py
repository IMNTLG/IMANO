# from flask import request, session
from test import app, db, request, session
# app.config['SECRET_KEY'] = 'dasdefaf9*&*Tfdad'
# conn = mysql.connector.connect(host='127.0.0.1', user='bbt',
#                                passwd='bbtbbtbbt', database='bbt_demo',
#                                charset='utf8mb4')
# db = conn.cursor()


@app.route('/bbt/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']

    db.execute('select `id` from users where `username`=%s and `password`=%s', (username, password))
    result = db.fetchone()

    if result:
        session['user_id'] = result[0]
        return {
            'errcode': 0,
            'errmsg': '登陆成功'
        }, 200
    return {
        'errcode': 401,
        'errmsg': '用户不存在或密码错误'
    }, 401
