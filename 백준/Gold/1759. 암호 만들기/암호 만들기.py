import sys
from itertools import combinations
input = sys.stdin.readline

def solution(L, C):
    v = ['a', 'e', 'i', 'o', 'u']
    lst = sorted(list(map(str, input().split())))
    
    all_pw = list(combinations(lst, L))
    res = []
    
    for pw in all_pw:
        check_c = 0
        check_v = 0
        tmp = ''
        for w in pw:
            if w in v:
                check_v += 1
            if w not in v:
                check_c += 1
                
        if check_v >= 1 and check_c >= 2:
            for p in pw:
                tmp += p
            res.append(tmp)
            
    return res

if __name__ == '__main__':
    L, C = map(int, input().split())
    ans = solution(L, C)
    for a in ans:
        print(a)