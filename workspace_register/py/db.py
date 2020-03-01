import mysql.connector
from flask import Flask

# 实例化一个Flask类, 同时为app设置secret_key
print('1111111')
app = Flask(__name__)
app.config['SECRET_KEY'] = 'dasdefaf9*&*Tfdad'  # 该secret_key为随机字符串
# 建立一个MySQL连接:

conn = mysql.connector.connect(host='127.0.0.1', user='bbt',
                               passwd='bbtbbtbbt', database='bbt_demo',
                               charset='utf8mb4')
db = conn.cursor()
username = 'lee'
db.execute('select username,password from users where username=\'gyn\'')
result = db.fetchall()
print(result)
