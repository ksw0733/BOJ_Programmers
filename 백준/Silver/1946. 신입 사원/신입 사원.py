import sys
input = sys.stdin.readline

def solution(lst):
    lst.sort()
    cnt = 1
    tmp = lst[0][1]
    
    for i in range(1, n):
        if tmp > lst[i][1]:
            cnt += 1
            tmp = lst[i][1]
    return cnt
    
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        lst = [list(map(int, input().split())) for _ in range(n)]
        print(solution(lst))