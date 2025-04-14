import sys
from collections import deque

input = sys.stdin.readline
        
def check_left(idx, dir):
    if idx < 0:
        return
    
    if gear[idx][2] != gear[idx + 1][6]:
        check_left(idx - 1, -dir)
        gear[idx].rotate(dir)
        
def check_right(idx, dir):
    if idx > 3:
        return
    
    if gear[idx - 1][2] != gear[idx][6]:
        check_right(idx + 1, -dir)
        gear[idx].rotate(dir)
        
def solution(gear, n):
    for _ in range(n):
        idx, dir = map(int, input().split())
        idx -= 1
        
        check_left(idx - 1, -dir)
        check_right(idx + 1, -dir)
        
        gear[idx].rotate(dir)
    
    score = 0
    
    for i in range(4):
        if gear[i][0] == '1':
            score += 2 ** i
            
    return score

if __name__ == "__main__":
    gear = [deque(input().rstrip()) for _ in range(4)]
    n = int(input())
    
    print(solution(gear, n))