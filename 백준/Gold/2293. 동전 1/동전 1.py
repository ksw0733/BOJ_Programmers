import sys
input = sys.stdin.readline

def solution(n, k):
    dp = [0] * (k + 1)
    coins = [int(input()) for _ in range(n)]
    dp[0] = 1
    
    for coin in coins:
        for i in range(coin, k + 1):
            dp[i] = dp[i] + dp[i - coin]
    
    return dp[k]
    
if __name__ == "__main__":
    n, k = map(int, input().split())
    print(solution(n, k))