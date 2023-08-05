from collections import deque

def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        queue = deque(skill)
        checkpoint = True
        
        for sk in tree:
            if sk not in queue:
                continue
                
            else:
                if sk == queue[0]:
                    queue.popleft()
                    
                else:
                    checkpoint = False
                    break
            
        if checkpoint:
            answer += 1
            
    return answer