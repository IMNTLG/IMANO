from flask import request, session
from flask import Flask
import mysql.connector
app = Flask(__name__, static_folder='D:/workspace/workspace2/')
app.config['SECRET_KEY'] = 'dasdefaf9*&*Tfdad'
conn = mysql.connector.connect(host='127.0.0.1', user='root',
                               passwd='000000', database='kou_mess',
                               charset='utf8mb4')
db = conn.cursor()
print('12345')
@app.route('/bbt/msg_delete', methods=['GET'])
def deletemsg():
    db.execute('select * from t_user')
    result = db.fetchall()
    if result:
        return {
            'errcode': 200,
            'errmsg': '',
            'data': result
        }, 200

# 关闭数据库连接
# db.close()


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9990)  # 将运行在本地回路ip的9990端口
