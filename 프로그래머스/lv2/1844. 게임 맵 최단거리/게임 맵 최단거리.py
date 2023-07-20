from collections import deque

def solution(maps):
    answer = bfs(0, 0, maps)

    return answer

def bfs(x, y, graph):
    q = deque()
    q.append((x, y))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    n = len(graph)
    m = len(graph[0])
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))
        
    if graph[n-1][m-1] == 1:
        return -1
        
    return graph[n-1][m-1]