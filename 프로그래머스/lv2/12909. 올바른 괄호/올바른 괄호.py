from collections import deque

def solution(s):
    q = deque()
    for ps in s:
        if ps == '(':
            q.append(ps)
        elif ps == ')' and len(q) == 0:
            q.append(ps)
            break
        else:
            q.pop()
            
    if len(q) == 0:
        return True
    else:
        return False