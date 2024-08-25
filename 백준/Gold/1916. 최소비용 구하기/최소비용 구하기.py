import sys
import heapq
input = sys.stdin.readline

def dijkstra(start, end, graph):
    INF = 1e8
    distance = [INF] * (N + 1)
    
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for next_node in graph[node]:
            cost = distance[node] + next_node[1]
            if cost < distance[next_node[0]]:
                distance[next_node[0]] = cost
                heapq.heappush(q, (cost, next_node[0]))    
                
    return distance[end]

if __name__ == '__main__':
    N = int(input())
    M = int(input())
    graph = [[] * (N + 1) for _ in range(N + 1)]
    
    for _ in range(M):
        start, end, cost = map(int, input().split())
        graph[start].append((end, cost))
        
    A, B = map(int, input().split())
    result = dijkstra(A, B, graph)
    print(result)