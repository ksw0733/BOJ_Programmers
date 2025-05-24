import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, visited):
    global answer
    answer = max(answer, len(visited))
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < C and 0 <= ny < R:
            ch = board[ny][nx]
            if ch not in visited:
                visited.add(ch)
                dfs(nx, ny, visited)
                visited.remove(ch)
    
    
R, C = map(int, input().split())
board = [list(map(str, input().rstrip())) for _ in range(R)]
answer = 0
visited = set()
visited.add(board[0][0])
dfs(0, 0, visited)

print(answer)