import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    if scoville[0] >= K:
        return 0
    
    while scoville[0] < K:
        
        if len(scoville) == 1:
            return -1
        
        a, b = heapq.heappop(scoville), heapq.heappop(scoville)
        
        new = a + (2 * b)
        heapq.heappush(scoville, new)
        answer += 1
         
    return answer