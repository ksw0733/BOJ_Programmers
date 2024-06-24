import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    time = list(map(int, input().split()))
    
    time.sort()
    res = 0
    for i in range(n):
        tmp = sum(time[:i+1])
        res += tmp
    print(res)