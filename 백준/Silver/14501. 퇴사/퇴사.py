import sys
input = sys.stdin.readline

def solution(n):
    for i in range(n - 1, -1, -1):
        if i + lst[i][0] > n:
            dp[i] = dp[i + 1]
        else:
            dp[i] = max(lst[i][1] + dp[i + lst[i][0]], dp[i + 1])
        
if __name__ == "__main__":
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]
    dp = [0] * (n + 1)
    solution(n)
    print(dp[0])