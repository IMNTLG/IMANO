from flask import request, session
from flask import Flask
import mysql.connector
app = Flask(__name__, static_folder='D:/workspace/workspace2/')
app.config['SECRET_KEY'] = 'dasdefaf9*&*Tfdad'
conn = mysql.connector.connect(host='127.0.0.1', user='root',
                               passwd='000000', database='kou_mess',
                               charset='utf8mb4')
db = conn.cursor()
@app.route('/bbt/msg_post', methods=['POST'])
def postmsg():
    data = request.get_json()
    username = data['username']
    postTimer = data['postTimer']
    msgBox = data['msgBox']
    db.execute('insert into t_user (fusername,fcreatetime,fnotes) values(%s, %s, %s)', (username, postTimer, msgBox))
    conn.commit()
    return {
        'errcode': 200,
        'errmsg': '提交成功'
    }, 200


# 关闭数据库连接
# db.close()


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9990)  # 将运行在本地回路ip的9990端口
