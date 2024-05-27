import sys
from collections import deque
input = sys.stdin.readline

def bfs(n, k):
    visited = [False] * (200001)
    q = deque()
    q.append([n, 0, [n]])
    visited[n] = True

    if n > k:
        return n - k, [int(x) for x in range(n, k - 1, -1)]


    while q:
        x, count, road = q.popleft()

        if x == k:
            return count, road

        arr = [x - 1, x + 1, x * 2]
        for a in arr:
            if 0 <= a <= 100000 and visited[a] == False:
                visited[a] = True
                r = road + [a]
                q.append([a, count + 1, r])
                
    
if __name__ == "__main__":
    n, k = map(int, input().split())
    count, pathes = bfs(n, k)
    print(count)
    for path in pathes:
        print(path, end=' ')
    