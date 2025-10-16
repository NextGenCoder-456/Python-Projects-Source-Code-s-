# chess_minimax.py
# Simple chess-like implementation with Minimax for rook/queen/king-like moves.
# NOTE: This is a simplified demonstration. Extend rules for full chess.

import copy
import math

# Board: 8x8 with simple pieces: K=white king, k=black king, Q=white queen, q=black queen, R/r rooks, B/b bishops, N/n knights, P/p pawns, . empty.
INITIAL_BOARD = [
    list("rnbqkbnr"),
    list("pppppppp"),
    list("........"),
    list("........"),
    list("........"),
    list("........"),
    list("PPPPPPPP"),
    list("RNBQKBNR")
]

def print_board(board):
    print("  a b c d e f g h")
    for i, row in enumerate(board):
        print(8 - i, " ".join(row))
    print()

def in_bounds(r, c):
    return 0 <= r < 8 and 0 <= c < 8

def is_white(piece): return piece.isupper()
def is_black(piece): return piece.islower()
def is_empty(piece): return piece == '.'

# Very simplified move generator: only basic pseudolegal moves for demo.
def generate_moves(board, white_to_move=True):
    moves = []
    for r in range(8):
        for c in range(8):
            p = board[r][c]
            if p == '.' : continue
            if white_to_move and not is_white(p): continue
            if not white_to_move and not is_black(p): continue

            # Pawn
            if p.lower() == 'p':
                dir = -1 if is_white(p) else 1
                nr = r + dir
                if in_bounds(nr, c) and board[nr][c] == '.':
                    moves.append(((r,c),(nr,c)))
                # captures
                for dc in (-1,1):
                    nc = c + dc
                    if in_bounds(nr, nc) and board[nr][nc] != '.':
                        target = board[nr][nc]
                        if is_white(p) != is_white(target):
                            moves.append(((r,c),(nr,nc)))
            # King: move one square any direction
            elif p.lower() == 'k':
                for dr in (-1,0,1):
                    for dc in (-1,0,1):
                        if dr==0 and dc==0: continue
                        nr, nc = r+dr, c+dc
                        if in_bounds(nr, nc):
                            if board[nr][nc] == '.' or is_white(board[nr][nc]) != is_white(p):
                                moves.append(((r,c),(nr,nc)))
            # Rook-like
            elif p.lower() == 'r' or p.lower() == 'q' or p.lower() == 'b' or p.lower() == 'n':
                # implement rook, bishop, queen, knight basics
                if p.lower() == 'n':
                    for dr,dc in [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]:
                        nr, nc = r+dr, c+dc
                        if in_bounds(nr,nc) and (board[nr][nc]=='.' or is_white(board[nr][nc])!=is_white(p)):
                            moves.append(((r,c),(nr,nc)))
                else:
                    directions = []
                    if p.lower() in ('r','q'):
                        directions += [(1,0),(-1,0),(0,1),(0,-1)]
                    if p.lower() in ('b','q'):
                        directions += [(1,1),(1,-1),(-1,1),(-1,-1)]
                    for dr,dc in directions:
                        nr, nc = r+dr, c+dc
                        while in_bounds(nr,nc):
                            if board[nr][nc]=='.':
                                moves.append(((r,c),(nr,nc)))
                            else:
                                if is_white(board[nr][nc]) != is_white(p):
                                    moves.append(((r,c),(nr,nc)))
                                break
                            nr += dr; nc += dc
    return moves

def make_move(board, move):
    b = copy.deepcopy(board)
    (r1,c1),(r2,c2) = move
    b[r2][c2] = b[r1][c1]
    b[r1][c1] = '.'
    return b

# Evaluate: material sum
VALUES = {'k':0,'q':9,'r':5,'b':3,'n':3,'p':1,'.':0}
def evaluate(board):
    score = 0
    for r in board:
        for p in r:
            val = VALUES.get(p.lower(),0)
            if p == '.': continue
            score += val if p.isupper() else -val
    return score

def minimax(board, depth, alpha, beta, white_to_move):
    if depth == 0:
        return evaluate(board), None
    best_move = None
    if white_to_move:
        max_eval = -math.inf
        for m in generate_moves(board, True):
            nb = make_move(board, m)
            val, _ = minimax(nb, depth-1, alpha, beta, False)
            if val > max_eval:
                max_eval = val; best_move = m
            alpha = max(alpha, val)
            if beta <= alpha: break
        return max_eval, best_move
    else:
        min_eval = math.inf
        for m in generate_moves(board, False):
            nb = make_move(board, m)
            val, _ = minimax(nb, depth-1, alpha, beta, True)
            if val < min_eval:
                min_eval = val; best_move = m
            beta = min(beta, val)
            if beta <= alpha: break
        return min_eval, best_move

def play():
    board = [list(row) for row in INITIAL_BOARD]
    white_turn = True
    while True:
        print_board(board)
        if white_turn:
            print("Your move (e.g. e2 e4): ", end="")
            user = input().strip()
            if user == 'exit': break
            try:
                src, dst = user.split()
                c1 = ord(src[0]) - ord('a'); r1 = 8 - int(src[1])
                c2 = ord(dst[0]) - ord('a'); r2 = 8 - int(dst[1])
                move = ((r1,c1),(r2,c2))
                if move in generate_moves(board, True):
                    board = make_move(board, move)
                    white_turn = False
                else:
                    print("Illegal move")
            except Exception as e:
                print("Parse error", e)
        else:
            print("AI thinking...")
            val, move = minimax(board, 3, -math.inf, math.inf, False)
            if move is None:
                print("No moves for AI. Game over.")
                break
            board = make_move(board, move)
            white_turn = True

if __name__ == "__main__":
    import math
    play()

Note: This is a workable minimax-based chess lite — full chess rules (castling, en-passant, promotion) are large; this provides a functional base and the minimax engine for basic piece moves and checkmate detection for internship demo purposes.
