import sys
input = sys.stdin.readline

def solution(n, graph):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i != j:
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    
    ans = 0
    tmp = float('inf')
    
    for i in range(n):
        if sum(graph[i]) < tmp:
            tmp = sum(graph[i])
            ans = i + 1
    return ans
                
if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[float('inf')] * n for _ in range(n)]
    
    for i in range(n):
        graph[i][i] = 0
        
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a-1][b-1], graph[b-1][a-1] = 1, 1
        
    print(solution(n, graph))
