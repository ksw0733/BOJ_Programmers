import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

R, C = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

visited_cache = set()

answer = 0

def dfs(x, y, mask, length):
    global answer
    
    if (x, y, mask) in visited_cache:
        return
    visited_cache.add((x, y, mask))

    answer = max(answer, length)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < C and 0 <= ny < R:
            ch = board[ny][nx]
            bit = ord(ch) - ord('A')

            if not (mask & (1 << bit)):
                dfs(nx, ny, mask | (1 << bit), length + 1)

start_bit = 1 << (ord(board[0][0]) - ord('A'))
dfs(0, 0, start_bit, 1)

print(answer)
