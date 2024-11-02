import sys
import heapq
input = sys.stdin.readline

def dijkstra(graph, K):
    distances = {node: float('inf') for node in graph}
    distances[K] = 0
    
    q = [(0, K)]
    
    while q:
        current_distance, current_node = heapq.heappop(q)
        
        if current_distance > distances[current_node]:
            continue
        
        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight
            
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(q, (distance, adjacent))
                
    return distances
    

if __name__ == '__main__':
    V, E = map(int, input().split())
    K = int(input())
    graph = {i: {} for i in range(1, V + 1)}
    for _ in range(E):
        u, v, w = map(int, input().split())
                
        if v not in graph[u] or graph[u][v] > w:
            graph[u][v] = w
    
    distance = dijkstra(graph, K)
    for key in distance:
        value = distance[key]
        if value == float('inf'):
            print('INF')
        else:
            print(value)