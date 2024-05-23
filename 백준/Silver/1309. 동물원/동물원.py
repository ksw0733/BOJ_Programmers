import sys
input = sys.stdin.readline

def solution(n, dp):
    if n == 1:
        return 3
    dp[1], dp[2] = 3, 7
    for i in range(3, n + 1):
        dp[i] = ((dp[i - 1] * 2) + dp[i - 2]) % 9901
        
    return dp[-1]
    
if __name__ == "__main__":
    n = int(input())
    dp = [0] * (n+1)
    ans = solution(n, dp)
    print(ans)