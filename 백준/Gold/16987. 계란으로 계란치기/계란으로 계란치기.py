import sys
input = sys.stdin.readline

def check_egg(eggs):
    cnt = 0
    for egg in eggs:
        if egg[0] <= 0:
            cnt += 1
    return cnt

def backtracking(depth, eggs):
    global ans
    if depth == N:
        ans = max(ans, check_egg(eggs))
        return
    
    if eggs[depth][0] <= 0:
        backtracking(depth + 1, eggs)
    else:
        isBroken = True
        for i in range(N):
            if depth != i and eggs[i][0] > 0:
                isBroken = False
                eggs[depth][0] -= eggs[i][1]
                eggs[i][0] -= eggs[depth][1]
                backtracking(depth + 1, eggs)
                eggs[depth][0] += eggs[i][1]
                eggs[i][0] += eggs[depth][1]
        if isBroken:
            backtracking(N, eggs)


N = int(input())
eggs = [list(map(int, input().split())) for _ in range(N)]
ans = 0
backtracking(0, eggs)
print(ans)