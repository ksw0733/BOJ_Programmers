import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def solution(n, k, l):
    if n == 0:
        return 0
    
    half = 2 ** (n - 1)
    if k < half and l < half:
        return solution(n - 1, k, l)
    elif k < half and l >= half:
        return half * half + solution(n - 1, k, l - half)
    elif k >= half and l < half:
        return 2 * half * half + solution(n - 1, k - half, l)
    else:
        return 3 * half * half + solution(n - 1, k - half, l - half)
    
if __name__ == "__main__":
    n, r, c = map(int, input().split())
    print(solution(n, r, c))