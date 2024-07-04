import sys
input = sys.stdin.readline

def solution(n):
    dp = [0] * (n + 1)
    if n < 3:
        return 1 if n == 1 else 2
    dp[1], dp[2] = 1, 2
    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2])%10007
    
    return dp[n]

if __name__ == "__main__":
    n = int(input())
    print(solution(n))