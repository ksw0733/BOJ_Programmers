import sys
from collections import deque
input = sys.stdin.readline

def calculation(num, order):
    if order == 'D':
        return (num * 2) % 10000
    if order == 'S':
        return 9999 if num == 0 else num - 1
    if order == 'L':
        return (num % 1000)*10 + num // 1000
    if order == 'R':
        return num // 10 + (num % 10)*1000

def solution(a, b):
    q = deque()
    visited = [False] * 10000
    commanders = ['D', 'S', 'L', 'R']
    q.append((a, ''))
    visited[a] = True
    while q:
        x, result = q.popleft()
        
        if x == b:
            return result
        
        for commander in commanders:
            new_x = calculation(x, commander)
            
            if not visited[new_x]:
                visited[new_x] = True
                q.append((new_x, result + commander))

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        print(solution(a, b))