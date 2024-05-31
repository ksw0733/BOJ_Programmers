import sys
input = sys.stdin.readline

def solution(n, lst):
    if n == 1:
        return max(lst[0][0], lst[1][0])
    
    else:
        dp = [[0] *  n for _ in range(2)]
        dp[0][0], dp[1][0] = lst[0][0], lst[1][0]
        dp[0][1], dp[1][1] = lst[1][0] + lst[0][1], lst[0][0] + lst[1][1]
        
        for i in range(2, n):
            dp[0][i] = max(dp[1][i - 1], dp[1][i - 2]) + lst[0][i]
            dp[1][i] = max(dp[0][i - 1], dp[0][i - 2]) + lst[1][i]
        
        return max(dp[0][-1], dp[1][-1])
    
if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        m = int(input())
        lst = [list(map(int, input().split())) for _ in range(2)]
            
        print(solution(m, lst))