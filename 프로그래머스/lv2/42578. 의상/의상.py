from collections import defaultdict

def solution(clothes):
    answer = 1
    item = defaultdict(int)
    
    for cloth, types in clothes:
        item[types] += 1
        
    for key in item:
        answer *= item[key] + 1
    
    return answer - 1