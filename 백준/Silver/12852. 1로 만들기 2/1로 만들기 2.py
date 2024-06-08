import sys
input = sys.stdin.readline

def solution(n):
    dp = [0] * (n + 1)
    path = [[] for _ in range(n + 1)]
    path[1] = [1]
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + 1
        path[i] = path[i - 1] + [i]
        
        if i % 2 == 0 and dp[i] > dp[i // 2] + 1:
            dp[i] = dp[i // 2] + 1
            path[i] = path[i // 2] + [i]
            
        if i % 3 == 0 and dp[i] > dp[i // 3] + 1:
            dp[i] = dp[i // 3] + 1
            path[i] = path[i // 3] + [i]
    
    return dp[n], path[n][::-1]
    
if __name__ == "__main__":
    n = int(input())
    result, sequence = solution(n)
    print(result)
    print(' '.join(map(str, sequence)))