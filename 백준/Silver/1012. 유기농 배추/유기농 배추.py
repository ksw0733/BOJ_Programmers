import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 1:
            graph[ny][nx] = -1
            dfs(nx, ny)
    

if __name__ == '__main__':
    t = int(input())
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    for _ in range(t):
        m, n, k = map(int, input().split())
        cnt = 0
        graph = [[0] * m for _ in range(n)]
        
        for _ in range(k):
            x, y = map(int, input().split())
            graph[y][x] = 1
        
        for i in range(m):
            for j in range(n):
                if graph[j][i] == 1:
                    dfs(i, j)
                    cnt += 1
                    
        print(cnt)