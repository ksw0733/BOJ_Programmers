from collections import Counter

def solution(k, tangerine):
    answer = 0
    tange_count = Counter(tangerine)
    tange_count = sorted(tange_count.items(), key = lambda x: x[-1], reverse = True)
    
    cnt = 0
    for _, v in tange_count:
        cnt += v
        answer += 1
        
        if cnt >= k:
            break

    return answer