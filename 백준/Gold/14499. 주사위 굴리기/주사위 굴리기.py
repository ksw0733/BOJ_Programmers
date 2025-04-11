import sys

input = sys.stdin.readline

N, M, y, x, o = map(int, input().split())
board = []

dice = [0, 0, 0, 0, 0, 0]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def turn(dir, dice):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    
    if dir == 1:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c
        
    elif dir == 2:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d
        
    elif dir == 3:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b
        
    else:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e
        
    return dice


for _ in range(N):
    board.append(list(map(int, input().split())))

order = list(map(int, input().split()))
    
ny, nx = y, x
for i in order:
    ny += dy[i - 1]
    nx += dx[i - 1]
    
    if nx < 0 or nx >= M or ny < 0 or ny >= N:
        ny -= dy[i - 1]
        nx -= dx[i - 1]
        continue
    
    turn(i, dice)
    
    if board[ny][nx] == 0:
        board[ny][nx] = dice[-1]
    else:
        dice[-1] = board[ny][nx]
        board[ny][nx] = 0
        
    print(dice[0])
    