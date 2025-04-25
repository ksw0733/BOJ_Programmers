import sys
input = sys.stdin.readline

def solution(trucks):
    time = 0
    bridge = [0 for _ in range(w)]
    
    while bridge:
        time += 1
        bridge.pop(0)
        if trucks:
            if sum(bridge) + trucks[0] <= L:
                bridge.append(trucks.pop(0))
            else:
                bridge.append(0)
            
    return time

if __name__ == "__main__":
    n, w, L = map(int, input().split())
    trucks = list(map(int, input().split()))
    print(solution(trucks))