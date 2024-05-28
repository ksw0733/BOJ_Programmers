import sys
from collections import deque
input = sys.stdin.readline

def solution(n, visited):
    q = deque()
    q.append((1, 0))
    while q:
        now, clip = q.popleft()
        if now == s:
            return visited[(now, clip)]
        if (now, now) not in visited.keys():
            visited[(now, now)] = visited[(now, clip)] + 1
            q.append((now, now))
        if (now + clip, clip) not in visited.keys():
            visited[(now + clip, clip)] = visited[(now, clip)] + 1
            q.append((now + clip, clip))
        if (now - 1, clip) not in visited.keys():
            visited[(now - 1, clip)] = visited[(now, clip)] + 1
            q.append((now - 1, clip))
    
if __name__ == "__main__":
    s = int(input())
    visited = {(1, 0): 0}
    print(solution(s, visited))