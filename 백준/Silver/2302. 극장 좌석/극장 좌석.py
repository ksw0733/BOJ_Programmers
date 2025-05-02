import sys
input = sys.stdin.readline
        
def solution(N, M):
    vip = [int(input()) for _ in range(M)]
    
    dp = [0] * (N + 1)
    if N == 1:
        return 1
    if N == 2:
        return 2
    dp[0], dp[1], dp[2] = 1, 1, 2
    for i in range(3, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    res = 1
    if M > 0:
        tmp = 0
        for i in range(M):
            res *= dp[vip[i] - 1 - tmp]
            tmp = vip[i]
        res *= dp[N - tmp]
    else:
        res = dp[N]
        
    return res
    
if __name__ == "__main__":
    N = int(input())
    M = int(input())
    print(solution(N, M))