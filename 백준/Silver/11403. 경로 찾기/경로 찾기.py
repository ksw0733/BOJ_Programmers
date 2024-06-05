import sys
input = sys.stdin.readline

def solution(n, graph):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = 1
    return graph
    
if __name__ == "__main__":
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    result = solution(n, graph)
    
    for row in result:
        print(' '.join(map(str, row)))