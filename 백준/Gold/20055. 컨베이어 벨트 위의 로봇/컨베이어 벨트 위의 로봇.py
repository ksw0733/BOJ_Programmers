import sys
from collections import deque
input = sys.stdin.readline

def solution(belt, N, K):
    cnt = 0
    check = 0
    robot = deque([False] * N)
    
    while check < K:
        belt.rotate(1)
        robot.rotate(1)
        robot[-1] = False
        
        for i in range(N - 1, 0, -1):
            if robot[i - 1] and not robot[i] and belt[i] != 0:
                robot[i] = True
                robot[i - 1] = False
                belt[i] -= 1
        
        robot[-1] = False
                
        if belt[0] != 0:
            robot[0] = True
            belt[0] -= 1
        
        cnt += 1
        
        check = belt.count(0)
        
    return cnt
    

if __name__ == "__main__":
    N, K = map(int, input().split())
    belt = deque(list(map(int, input().split())))
    res = solution(belt, N, K)
    print(res)