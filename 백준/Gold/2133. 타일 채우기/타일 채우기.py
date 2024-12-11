import sys
input = sys.stdin.readline

def dp(N):
    dp = [0] * 31
    dp[2] = 3
    for i in range(4, N + 1):
        if i % 2 == 1:
            continue
        else:
            dp[i] = dp[i - 2] * 3 + sum(dp[:i - 2]) * 2 + 2
            
    return dp[N]

if __name__ == '__main__':
    N = int(input())
    print(dp(N))