# client.py
import socket, threading

client = socket.socket()
client.connect(('localhost', 5555))

def receive():
    while True:
        try:
            msg = client.recv(1024).decode()
            print("\n" + msg)
        except:
            break

threading.Thread(target=receive).start()

while True:
    client.send(input("You: ").encode())
