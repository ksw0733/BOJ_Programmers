import sys
input = sys.stdin.readline

def solution(n, lst, dp):
    dp[0] = lst[0]
    for i in range(n):
        for j in range(i):
            if lst[i] > lst[j]:
                dp[i] = max(dp[i], dp[j] + lst[i])
            else:
                dp[i] = max(dp[i], lst[i])
    return max(dp)
    
if __name__ == "__main__":
    n = int(input())
    lst = list(map(int, input().split()))
    dp = [0] * n
    ans = solution(n, lst, dp)
    print(ans)