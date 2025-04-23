import sys
from collections import Counter
from functools import reduce
input = sys.stdin.readline

def cal_R(arr):
    mx = 0
    for i in range(len(arr)):
        x = Counter(arr[i])
        del x[0]
        x = list(x.items())
        x.sort(key = lambda x: (x[1], x[0]))
        if len(x) > 50:
            x = x[:50]
        arr[i] = reduce(lambda x, y: list(x) + list(y), x[1:], list(x[0]))
        mx = max(mx, len(arr[i]))
    
    for i in range(len(arr)):
        if len(arr[i]) < mx:
            arr[i].extend([0] * (mx - len(arr[i])))
            
def solution(arr):
    time = 0
    if R < len(arr) and C < len(arr[0]):
        if arr[R][C] == K:
            return time
    
    while time <= 100:
        if len(arr) >= len(arr[0]):
            cal_R(arr)
        else:
            arr = list(map(list, zip(*arr)))
            cal_R(arr)
            arr = list(map(list, zip(*arr)))
        time += 1
        if R < len(arr) and C < len(arr[0]):
            if arr[R][C] == K:
                return time
    
    return -1

if __name__ == "__main__":
    R, C, K = map(int, input().split())
    R, C = R - 1, C - 1
    arr = [list(map(int, input().split())) for _ in range(3)]
    
    print(solution(arr))