import sys
input = sys.stdin.readline
INF = sys.maxsize

def solution(board):
    dist = [[INF] * N for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            dist[i][j] = board[i][j]
            
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist


N = int(input())
M = int(input())
board = [[INF] *  N for _ in range(N)]
for _ in range(M):
    start, arrive, c = map(int, input().split())
    c = min(board[start - 1][arrive - 1], c)
    board[start - 1][arrive - 1] = c
    
for i in range(N):
    for j in range(N):
        if i == j:
            board[i][j] = 0

answer = solution(board)

for i in range(N):
    for j in range(N):
        if answer[i][j] == INF:
            answer[i][j] = 0

for ans in answer:
    print(*ans, sep = ' ')