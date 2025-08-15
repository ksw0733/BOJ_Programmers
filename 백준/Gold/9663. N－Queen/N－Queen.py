import sys
input = sys.stdin.readline

def dfs(row):
    global result
    
    if row == N:
        result += 1
        return
    
    for col in range(N):
        if not is_col_used[col] and \
           not is_diag1_used[row + col] and \
           not is_diag2_used[row - col + N - 1]:
            
            is_col_used[col] = True
            is_diag1_used[row + col] = True
            is_diag2_used[row - col + N - 1] = True
            
            dfs(row + 1)
            
            is_col_used[col] = False
            is_diag1_used[row + col] = False
            is_diag2_used[row - col + N - 1] = False

N = int(input())
result = 0


is_col_used = [False] * N
is_diag1_used = [False] * (2 * N - 1)
is_diag2_used = [False] * (2 * N - 1)

dfs(0)
print(result)