import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())
    lst = [0] + list(map(int, input().split()))
    prefix_sum = [0] * (n+1)
    for i in range(1, n+1):
        prefix_sum[i] = prefix_sum[i-1] + lst[i]
    for _ in range(m):
        a, b = map(int, input().split())
        print(prefix_sum[b] - prefix_sum[a-1])