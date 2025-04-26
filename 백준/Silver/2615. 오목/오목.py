import sys
input = sys.stdin.readline

def solution(board):
    move = [(1, 0), (1, 1), (0, 1), (-1, 1)]
    
    for i in range(19):
        for j in range(19):
            if board[i][j] != 0:
                stone = board[i][j]
                for dy, dx in move:
                    ny, nx, check = i + dy, j + dx, 1
                    while 0 <= ny < 19 and 0 <= nx < 19 and board[ny][nx] == stone:
                        check += 1
                        if check == 5:
                            if 0 <= i - dy < 19 and 0 <= j - dx < 19 and board[i - dy][j - dx] == stone:
                                break
                            if 0 <= ny + dy < 19 and 0 <= nx + dx < 19 and board[ny + dy][nx + dx] == stone:
                                break
                            if stone == 1:
                                return 1, i + 1, j + 1
                            if stone == 2:
                                return 2, i + 1, j + 1
                        ny += dy
                        nx += dx
        
    return 0, 0, 0 

if __name__ == "__main__":
    board = [list(map(int, input().split())) for _ in range(19)]
    win, y, x = solution(board)
    if win > 0:
        print(win)
        print(y, x)
    else:
        print(win)