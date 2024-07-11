import sys
input = sys.stdin.readline
from collections import deque

if __name__ == "__main__":
    n, k = map(int, input().split())
    coins = deque()
    for _ in range(n):
        coins.appendleft(int(input()))
        
    answer = 0
    while coins:
        value = coins.popleft()
        if value > k:
            pass
        else:
            tmp = k // value
            answer += tmp
            k -= value * tmp
    
    print(answer)