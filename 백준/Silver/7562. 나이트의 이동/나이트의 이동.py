import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y, x_goal, y_goal):
    q = deque()
    q.append([x, y])
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        if x == x_goal and y == y_goal:
            return visited[x][y] - 1
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < m:
                if visited[nx][ny] == 0:
                    q.append([nx, ny])
                    visited[nx][ny] = visited[x][y] + 1

if __name__ == '__main__':
    n = int(input())
    dx = [1, -1, 1, -1, 2, -2, 2, -2]
    dy = [2, 2, -2, -2, 1, 1, -1, -1]
    
    for _ in range(n):
        m = int(input())
        visited = [[0] * m for _ in range(m)]
        x, y = map(int, input().split())
        x_goal, y_goal = map(int, input().split())
        ans = bfs(x, y, x_goal, y_goal)
        print(ans)