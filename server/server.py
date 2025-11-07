from flask import Flask, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")
users = {}

@socketio.on('join')
def handle_join(data):
    user = data['user']
    users[user] = request.sid
    emit('server_message', {'msg': f"{user} joined the chat"}, broadcast=True)

@socketio.on('send_message')
def handle_message(data):
    emit('receive_message', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='127.0.0.1', port=5000, debug=True)
