import sys
from itertools import combinations
input = sys.stdin.readline

def sol(start, link):
    start_stat, link_stat = 0, 0
    for i in range(N // 2):
        for j in range(N // 2):
            start_stat += stat[start[i]][start[j]]
            link_stat += stat[link[i]][link[j]]
            
    return abs(start_stat - link_stat)
    

N = int(input())
stat = []
res = []
for _ in range(N):
    stat.append(list(map(int, input().split())))

for i in combinations(list(range(N)), N//2):
    start_idx = i
    link_idx = list(set(list(range(N))) - set(start_idx))
    res.append(sol(start_idx, link_idx))
    
print(min(res))