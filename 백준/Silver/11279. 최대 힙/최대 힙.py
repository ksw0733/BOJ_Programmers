import sys
input = sys.stdin.readline
import heapq

if __name__ == "__main__":
    n = int(input())
    lst = []
    for _ in range(n):
        m = int(input())
        if m == 0:
            if len(lst) == 0:
                print(0)
            else:
                print(-heapq.heappop(lst))
        else:
            heapq.heappush(lst, -m)