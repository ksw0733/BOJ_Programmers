import sys
input = sys.stdin.readline

def solution(n):
    dp = [0] * (n + 1)
    if n == 1:
        return 1
    if n == 2:
        return 3
    
    dp[1] = 1
    dp[2] = 3
    
    for i in range(3, n + 1):
        dp[i] = (2*dp[i-2] + dp[i-1]) % 10007
        
    return dp[n]

if __name__ == "__main__":
    n = int(input())
    print(solution(n))