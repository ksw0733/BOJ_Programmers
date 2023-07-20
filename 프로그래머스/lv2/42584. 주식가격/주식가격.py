from collections import deque

def solution(prices):
    answer = []
    queue = deque(prices)
    
    while queue:
        tmp = 0
        price = queue.popleft()
        
        for q in queue:
            tmp += 1
            if q < price:
                break
                
        answer.append(tmp)
        
    return answer