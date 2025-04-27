import sys
input = sys.stdin.readline

def solution(board, N):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    if N == 1:
        return board
    
    if N % 2 == 0:
        ans = [['O'] * C for _ in range(R)]    
        return ans
    
    elif N % 4 == 3:
        tmp = [['O'] * C for _ in range(R)]
        for i in range(R):
            for j in range(C):
                if board[i][j] == 'O':
                    tmp[i][j] = '.'
                    for k in range(4):
                        nx = j + dx[k]
                        ny = i + dy[k]
                        if 0 <= ny < R and 0 <= nx < C:
                            tmp[ny][nx] = '.'
                    
        return tmp
    
    else:
        tmp = [['O'] * C for _ in range(R)]
        for i in range(R):
            for j in range(C):
                if board[i][j] == 'O':
                    tmp[i][j] = '.'
                    for k in range(4):
                        nx = j + dx[k]
                        ny = i + dy[k]
                        if 0 <= ny < R and 0 <= nx < C:
                            tmp[ny][nx] = '.'
        
        tmp2 = [['O'] * C for _ in range(R)]
        for i in range(R):
            for j in range(C):
                if tmp[i][j] == 'O':
                    tmp2[i][j] = '.'
                    for k in range(4):
                        nx = j + dx[k]
                        ny = i + dy[k]
                        if 0 <= ny < R and 0 <= nx < C:
                            tmp2[ny][nx] = '.'
        
        return tmp2
            

if __name__ == "__main__":
    R, C, N = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(R)]
    res = solution(board, N)
    for ans in res:
        print(''.join(ans))