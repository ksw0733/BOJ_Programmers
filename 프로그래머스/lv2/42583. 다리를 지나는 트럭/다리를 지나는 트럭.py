from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    cnt = 0
    current_weight = 0
    bridge = deque([0] * bridge_length)
    
    while bridge:
        current_weight -= bridge.popleft()
        answer += 1
        
        if truck_weights:
            if current_weight + truck_weights[0] <= weight:
                truck = truck_weights.pop(0)
                bridge.append(truck)
                current_weight += truck
            else:
                bridge.append(0)
                
    return answer