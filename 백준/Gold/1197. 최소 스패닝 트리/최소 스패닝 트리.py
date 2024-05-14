import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

def prim(graph, v):
    cnt = 0
    ans = 0
    
    while cnt < v:
        weight, vertex = heapq.heappop(queue)
        
        if not visited[vertex]:
            visited[vertex] = True
            ans += weight
            cnt += 1
            for dot, value in graph[vertex]:
                if not visited[dot]:
                    heapq.heappush(queue, (value, dot))
    return ans

if __name__ == '__main__':
    v, e = map(int, input().split())
    graph = defaultdict(list)
    visited = [False for _ in range(v)]
    queue = [(0, 0)]
    for _ in range(e):
        dot1, dot2, weight = map(int, input().split())
        graph[dot1-1].append([dot2-1, weight])
        graph[dot2-1].append([dot1-1, weight])
    
    res = prim(graph, v)
    print(res)