import sys
input = sys.stdin.readline

def solution(N, S, M):
    volum = list(map(int, input().split()))
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    dp[0][S] = 1
    
    for i in range(N):
        for j in range(M + 1):
            if dp[i][j] == 1:
                min_val = j - volum[i]
                max_val = j + volum[i]
                
                if min_val >= 0:
                    dp[i + 1][min_val] = 1
                if max_val <= M:
                    dp[i + 1][max_val] = 1
                    
    for i in range(M, -1, -1):
        if dp[N][i] == 1:
            return i
    
    return -1
        
if __name__ == "__main__":
    N, S, M = map(int, input().split())
    print(solution(N, S, M))