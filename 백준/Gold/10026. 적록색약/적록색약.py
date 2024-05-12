
import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

def dfs(x, y):
    visited[x][y] = True
    current_color = graph[x][y]
    
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < n:
            if visited[nx][ny] == False:
                if graph[nx][ny] == current_color:
                    dfs(nx, ny)

if __name__ == '__main__':
    n = int(input())
    graph = [list(input().rstrip()) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    normal, c_weak = 0, 0
    
    for i in range(n):
        for j in range(n):
            if visited[i][j] == False:
                dfs(i, j)
                normal += 1
    
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'R':
                graph[i][j] = 'G'
                
    visited = [[False] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if visited[i][j] == False:
                dfs(i, j)
                c_weak += 1
                
    print(normal, c_weak)