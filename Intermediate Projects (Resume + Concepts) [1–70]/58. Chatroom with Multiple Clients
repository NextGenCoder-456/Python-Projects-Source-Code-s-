# server.py
import socket, threading

clients = []

def handle(client):
    while True:
        try:
            msg = client.recv(1024).decode()
            for c in clients:
                if c != client:
                    c.send(msg.encode())
        except:
            clients.remove(client)
            break

server = socket.socket()
server.bind(('localhost', 5555))
server.listen()

print("Server started...")

while True:
    client, _ = server.accept()
    clients.append(client)
    threading.Thread(target=handle, args=(client,)).start()
