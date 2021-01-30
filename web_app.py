from flask import Flask, request
from db_connector import insert, select, update, delete
import os
import signal

app = Flask(__name__)

# supported methods
@app.route('/users/get_user_data/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user(user_id):
    try:
        user_name = select(user_id)
        return "<H1 id='user'>" + user_name + "</H1>"
    except Exception as e:
        print(e)
        return "<H1 id='error'>no such user: "+ user_id + "</H1>"

@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return 'Server stopped'


app.run(host='127.0.0.1', debug=True, port=5001)