# ttt_client.py
import socket, threading

HOST = '127.0.0.1'
PORT = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

mark = None
board = [' ']*9

def listen():
    global mark, board
    while True:
        data = s.recv(1024).decode()
        if not data: break
        if data.startswith("MARK:"):
            mark = data.split(":")[1]
            print("Your mark:", mark)
        elif data.startswith("BOARD:"):
            board = list(data.split(":")[1])
            print_board()
        elif data.startswith("RESULT:"):
            res = data.split(":")[1]
            if res == 'D':
                print("Draw!")
            else:
                print("Winner:", res)
            s.close()
            break

def print_board():
    print()
    for i in range(3):
        row = board[3*i:3*i+3]
        print("|".join(row))
    print()

threading.Thread(target=listen, daemon=True).start()

while True:
    cmd = input("Enter move (0-8): ")
    if cmd.isdigit():
        s.sendall(("MOVE:"+cmd).encode())
    else:
        print("Bad input")
