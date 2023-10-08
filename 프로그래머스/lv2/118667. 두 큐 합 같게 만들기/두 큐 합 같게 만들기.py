from collections import deque

def solution(queue1, queue2):
    answer = 0
    q1 = deque(queue1)
    q2 = deque(queue2)
    s1, s2 = sum(q1), sum(q2)
    
    if (s1 + s2) % 2 == 1:
        return -1
    
    while True:
        if answer == 4 * len(q1):
            return -1
        
        if s1 > s2:
            tmp = q1.popleft()
            s1 -= tmp
            s2 += tmp
            q2.append(tmp)
            answer += 1
            
        elif s1 < s2:
            tmp = q2.popleft()
            s1 += tmp
            s2 -= tmp
            q1.append(tmp)
            answer += 1
            
        else:
            break
            
    return answer