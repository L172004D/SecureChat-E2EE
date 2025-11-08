from flask import Flask
from flask_socketio import SocketIO, send
from cryptography.fernet import Fernet

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

# Generate encryption key for E2EE
key = Fernet.generate_key()
cipher = Fernet(key)

@socketio.on('message')
def handle_message(msg):
    print(f"Received message: {msg}")
    send(msg, broadcast=True)

if __name__ == '__main__':
    print("✅ Server running at: http://127.0.0.1:5000")
    socketio.run(app, host="0.0.0.0", port=5000)
