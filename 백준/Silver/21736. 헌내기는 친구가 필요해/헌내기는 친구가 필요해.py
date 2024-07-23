import sys
from collections import deque
input = sys.stdin.readline

def solution(campus, now, n, m):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    visited = [[False] * m for _ in range(n)]
    q = deque()
    q.append(now)
    cnt = 0
    
    while q:
        y, x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx] and campus[ny][nx] != 'X':
                visited[ny][nx] = True
                q.append((ny, nx))
                if campus[ny][nx] == 'P':
                    cnt += 1
                
    return cnt if cnt != 0 else 'TT'
    

if __name__ == '__main__':
    n, m = map(int, input().split())
    campus = []
    for i in range(n):
        tmp = str(input().rstrip())
        if tmp.find('I') != -1:
            doyeon = (i, tmp.find('I'))
        campus.append(list(tmp))
    
    print(solution(campus, doyeon, n, m))