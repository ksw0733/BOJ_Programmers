import sys
input = sys.stdin.readline

def backtracking(L, w):
    if len(L) == 2:
        return w
    
    res = 0
    for i in range(1, len(L) - 1):
        na = L[:i] + L[i + 1:]
        tmp = backtracking(na, w + L[i - 1] * L[i + 1])
        if res < tmp:
            res = tmp

    return  res

if __name__ == '__main__':
    N = int(input())
    L = list(map(int, input().split()))
    print(backtracking(L, 0))