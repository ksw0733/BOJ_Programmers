import sys
input = sys.stdin.readline

def solution(N):
    board = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0] * N for _ in range(N)]
    dp[0][0] = 1
    
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                return dp[-1][-1]
            move = board[i][j]
            if i + move < N:
                dp[i + move][j] += dp[i][j]
            if j + move < N:
                dp[i][j + move] += dp[i][j]
        
if __name__ == "__main__":
    N = int(input())
    print(solution(N))