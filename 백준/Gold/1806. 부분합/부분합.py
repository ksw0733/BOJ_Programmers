import sys
input = sys.stdin.readline

def solution(M, lst):
    end = 0
    tmp = 0
    answer = N + 1
    
    for start in range(N):
        while tmp < M and end < N:
           tmp += lst[end]
           end += 1
        if tmp >= M:
            answer = min(answer, end - start)
        tmp -= lst[start]
    return print(0) if sum(lst) < M else print(answer) 

N, M = map(int, input().split())
lst = list(map(int, input().split()))
solution(M, lst)