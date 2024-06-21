import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())
    trees = list(map(int, input().split()))
    
    start, end = 1, max(trees)
    
    while start <= end:
        mid = (start + end) // 2
        length = sum([tree - mid for tree in trees if tree > mid])

        if length < m:
            end = mid - 1
        else:
            start = mid + 1
    
    print(end)