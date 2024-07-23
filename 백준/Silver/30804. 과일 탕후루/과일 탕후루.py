import sys
from collections import defaultdict
input = sys.stdin.readline

def solution(tanghuru, n):
    start = 0
    end = 0
    kind = 0
    fruit = defaultdict(int)
    ans = 0
    while end < n:
        if fruit[tanghuru[end]] == 0:
            kind += 1
        fruit[tanghuru[end]] += 1
        
        while kind > 2:
            fruit[tanghuru[start]] -= 1
            if fruit[tanghuru[start]] == 0:
                kind -= 1
            start += 1
        ans = max(ans, end - start + 1)
        end += 1
    
    return ans
    

if __name__ == '__main__':
    n = int(input())
    tanghuru = list(map(int, input().split()))
    print(solution(tanghuru, n))