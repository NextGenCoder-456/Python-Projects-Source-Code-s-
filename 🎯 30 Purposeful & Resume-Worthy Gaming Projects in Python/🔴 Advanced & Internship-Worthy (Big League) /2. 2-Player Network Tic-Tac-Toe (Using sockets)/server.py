# ttt_server.py
import socket
import threading

HOST = '0.0.0.0'
PORT = 9999

clients = []
board = [' '] * 9
lock = threading.Lock()

def check_win(b):
    wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for a,b1,c in wins:
        if b[a]==b[b1]==b[c] and b[a] != ' ':
            return b[a]
    if ' ' not in b:
        return 'D'  # draw
    return None

def handle(conn, addr, mark):
    conn.sendall(f"MARK:{mark}".encode())
    while True:
        try:
            data = conn.recv(1024).decode()
            if not data: break
            if data.startswith("MOVE:"):
                pos = int(data.split(":")[1])
                with lock:
                    if board[pos] == ' ':
                        board[pos] = mark
                        # broadcast
                        for c in clients:
                            c.sendall(("BOARD:" + "".join(board)).encode())
                        winner = check_win(board)
                        if winner:
                            for c in clients:
                                c.sendall(("RESULT:" + winner).encode())
        except:
            break
    conn.close()

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(2)
    print("Server listening", HOST, PORT)
    marks = ['X','O']
    while len(clients) <2:
        conn, addr = s.accept()
        clients.append(conn)
        print("Client connected", addr)
        threading.Thread(target=handle, args=(conn, addr, marks[len(clients)-1])).start()

if __name__ == "__main__":
    main()
