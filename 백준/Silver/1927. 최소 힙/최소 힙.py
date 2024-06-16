import sys
input = sys.stdin.readline
import heapq

def solution(n):
    heap = []
    for _ in range(n):
        x = int(input())
        if x == 0:
            if not heap:
                print(0)
            else:
                print(heapq.heappop(heap))
        if x > 0:
            heapq.heappush(heap, x)
                
if __name__ == "__main__":
    n = int(input())
    solution(n)