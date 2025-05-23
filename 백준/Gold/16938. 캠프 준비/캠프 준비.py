import sys
input = sys.stdin.readline

def backtracking(idx, count, total, min_val, max_val):
    global answer
    
    if idx == N:
        if count >= 2 and L <= total <= R and (max_val - min_val) >= X:
            answer +=1
        return
    
    backtracking(idx + 1, count, total, min_val, max_val)
    
    curr = problems[idx]
    new_min = min(curr, min_val) if count > 0 else curr
    new_max = max(curr, max_val) if count > 0 else curr
    backtracking(idx + 1, count + 1, total + curr, new_min, new_max)
    
    
N, L, R, X = map(int, input().split())
problems = list(map(int, input().split()))
answer = 0

backtracking(0, 0, 0, 0, 0)
print(answer)