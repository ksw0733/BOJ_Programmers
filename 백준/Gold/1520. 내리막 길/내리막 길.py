import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x, y, N, M, graph, dp):
    
    if dp[y][x] != -1:
        return dp[y][x]
    
    dp[y][x] = 0
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < M and 0 <= ny < N and graph[ny][nx] < graph[y][x]:
            dp[y][x] += dfs(nx, ny, N, M, graph, dp)
    
    return dp[y][x]

def solution(N, M):
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))
    
    dp = [[-1 for _ in range(M)] for _ in range(N)]
    dp[N-1][M-1] = 1
    
    dfs(0, 0, N, M, graph, dp)
    
    return dp[0][0]

if __name__ == '__main__':
    N, M = map(int, input().split())
    print(solution(N, M))