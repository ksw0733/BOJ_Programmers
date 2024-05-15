import sys
input = sys.stdin.readline

def solution(n):
    for i in range(n):
        dp[i] = card_pack[i]
        for j in range(i):
            dp[i] = max(dp[i], dp[i - j - 1] + card_pack[j])
            
    return dp[-1]
        
if __name__ == "__main__":
    n = int(input())
    card_pack = list(map(int, input().split()))
    dp = [0] * n
    print(solution(n))