import sys
from collections import deque
input = sys.stdin.readline

def solution():
    N, K = map(int, input().split())
    d = list(map(int, input().split()))
    graph = [[] for _ in range(N + 1)]
    inDegree = [0 for _ in range(N + 1)]
    dp = [0 for _ in range(N + 1)]
    q = deque()
    
    for i in range(K):
        a, b = map(int, input().split())
        graph[a].append(b)
        inDegree[b] += 1
        
    w = int(input())
    
    for i in range(1, N + 1):
        if inDegree[i] == 0:
            q.append(i)
            dp[i] = d[i - 1]
    
    while q:
        tmp = q.popleft()
        
        for i in graph[tmp]:
            inDegree[i] -= 1
            dp[i] = max(dp[i], dp[tmp] + d[i - 1])
            if inDegree[i] == 0:
                q.append(i)
    
    return dp[w]

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        print(solution())