import sys
input = sys.stdin.readline

def dp(coins, k):
    INF = int(10001)
    dp = [INF] * (k + 1)
    dp[0] = 0
    
    for coin in coins:
        for i in range(coin, k + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[k] if dp[k] != INF else -1

if __name__ == '__main__':
    n, k = map(int, input().split())
    coins = []
    for i in range(n):
        coins.append(int(input()))
    print(dp(coins, k))