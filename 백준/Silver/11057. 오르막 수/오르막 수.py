import sys
input = sys.stdin.readline

def solution(n):
    dp = [1] * 10
    for _ in range(n-1):
        for j in range(1, 10):
            dp[j] += dp[j-1]
            
    return sum(dp) % 10007
    
if __name__ == "__main__":
    n = int(input())
    print(solution(n))