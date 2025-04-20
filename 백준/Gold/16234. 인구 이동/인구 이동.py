import sys
from collections import deque
input = sys.stdin.readline

def check_union(land, visited, L, R, y, x):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    q = deque([(y, x)])
    lst = [(y, x)]
    
    while q:
        y, x = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if ny >= N or nx >= N or ny < 0 or nx < 0 or visited[ny][nx]:
                continue
            
            if L <= abs(land[y][x] - land[ny][nx]) <= R and not visited[ny][nx]:
                visited[ny][nx] = True
                q.append((ny, nx))
                lst.append((ny, nx))
    
    if len(lst) <= 1:
        return 0
    
    res = sum(land[y][x] for y, x in lst) // len(lst)
    for y, x in lst:
        land[y][x] = res

    return 1

if __name__ == "__main__":
    N, L, R = map(int, input().split())
    land = [list(map(int, input().split())) for _ in range(N)]
    
    day = 0
    while 1:
        check = 0
        visited = [[False] * N for _ in range(N)]
        
        for j in range(N):
            for i in range(N):
                if not visited[j][i]:
                    visited[j][i] = True
                    check += check_union(land, visited, L, R, j, i)
        if check == 0:
            break
        
        day += 1
    
    print(day)