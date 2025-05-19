import sys
input = sys.stdin.readline

N, K = map(int, input().split())

cnt = 0
found = False

def backtracking(path, total):
    global cnt, found
    
    if found:
        return
    
    if total == N:
        cnt += 1
        if cnt == K:
            print('+'.join(map(str, path)))
            found = True
        return
    
    elif total > N:
        return
    
    for i in [1, 2, 3]:
        backtracking(path + [i], total + i)

backtracking([], 0)
if not found:
    print(-1)