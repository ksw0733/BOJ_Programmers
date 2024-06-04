import sys
input = sys.stdin.readline

def solution(n, k, l):
    res = 1
    n = n % l
    while k > 0:
        if k % 2 == 1:
            res = (res * n) % l
        k = k // 2
        n = (n * n) % l
        
    return res
    
if __name__ == "__main__":
    n, k, l = map(int, input().split())
    print(solution(n, k, l))