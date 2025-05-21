import sys
input = sys.stdin.readline

N = int(input())

def is_prime(N):
    for i in range(2, int(N ** 0.5) + 1):
        if N % i == 0:
            return False
    return True

def backtracking(num, ans):
    global N
    
    if is_prime(num):
        if len(str(num)) == N:
            ans.append(num)
            return
        
        for i in range(1, 10):
            tmp = int(str(num) + str(i))
            if is_prime(tmp):
                backtracking(tmp, ans)

lst = [2, 3, 5, 7]
res = []
for i in lst:
    backtracking(i, res)

print(*res, sep='\n')