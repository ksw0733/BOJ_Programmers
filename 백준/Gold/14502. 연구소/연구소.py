import sys
from collections import deque
import copy
input = sys.stdin.readline

def check_safety(graph, N, K):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    lap_map = copy.deepcopy(graph)
    q = deque()
    
    for x in range(N):
        for y in range(K):
            if lap_map[x][y] == 2:
                q.append((x, y))
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < K and lap_map[nx][ny] == 0:
                lap_map[nx][ny] = 2
                q.append((nx, ny))
    
    safezone = 0
    for line in lap_map:
        safezone += line.count(0)
        
    return safezone

def make_wall(wall_cnt, result, N, K):
    if wall_cnt == 3:
        return check_safety(graph, N, K)
    
    max_result = result
    for x in range(N):
        for y in range(K):
            if graph[x][y] == 0:
                graph[x][y] = 1
                max_result = max(max_result, make_wall(wall_cnt + 1, result, N, K))
                graph[x][y] = 0
                
    return max_result

if __name__ == '__main__':
    N, K = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    ans = make_wall(0, 0, N, K)
    print(ans)