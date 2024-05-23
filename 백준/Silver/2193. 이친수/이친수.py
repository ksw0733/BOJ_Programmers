import sys
input = sys.stdin.readline

def solution(n, dp):
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

if __name__ == "__main__":
    n = int(input())
    dp = [0] * (n+1)
    solution(n, dp)
    print(dp[-1])