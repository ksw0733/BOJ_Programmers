import sys
input = sys.stdin.readline

def solution(m, n, x, y):
    k = x
    while k <= m * n:
        if (k-x) % m == 0 and (k-y) % n == 0:
            return k
        k += m
    return -1

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        m, n, x, y = map(int, input().split())
        
        print(solution(m, n, x, y))