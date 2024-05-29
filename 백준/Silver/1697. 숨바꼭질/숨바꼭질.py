import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
queue = deque()
graph = [0] * 100001

def bfs():
    queue.append(n)
    while queue:
        x = queue.popleft()
        if x == k:
            return graph[k]
        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx <= 100000 and graph[nx] == 0:
                graph[nx] = graph[x] + 1
                queue.append(nx)

bfs()

print(graph[k])