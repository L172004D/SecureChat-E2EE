import socketio
import threading
from crypto_utils import generate_keys, rsa_encrypt, rsa_decrypt, aes_encrypt, aes_decrypt
import os
import base64

SERVER = "http://127.0.0.1:5000"

class ChatClient:
    def __init__(self, username):
        self.username = username
        self.sio = socketio.Client()
        self.private_key, self.public_key = generate_keys()
        self.sio.on('receive_message', self.on_message)
        self.sio.connect(SERVER)
        import time; time.sleep(1)
        self.sio.emit('join', {'user': username})

    def on_message(self, data):
        print(f"\n{data['user']}: {data['msg']}")

    def send_message(self, msg):
        self.sio.emit('send_message', {'user': self.username, 'msg': msg})

if __name__ == "__main__":
    client = ChatClient('alice')
    while True:
        msg = input("You: ")
        client.send_message(msg)
