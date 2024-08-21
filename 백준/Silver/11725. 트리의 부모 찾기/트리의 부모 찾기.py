import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit = 1000000

def find_parents(N, tree):
    parents = [0] * (N + 1)
    queue = deque([1])
    parents[1] = 1
    
    while queue:
        node = queue.popleft()
        for neighbor in tree[node]:
            if parents[neighbor] == 0:
                parents[neighbor] = node
                queue.append(neighbor)
    return parents

def solution():
    N = int(input())
    tree = [[] for _ in range(N + 1)]
    
    for _ in range(N - 1):
        u, v = map(int, input().split())
        tree[u].append(v)
        tree[v].append(u)
    parents = find_parents(N, tree)
    
    for i in range(2, N + 1):
        print(parents[i])
        

if __name__ == '__main__':
    solution()