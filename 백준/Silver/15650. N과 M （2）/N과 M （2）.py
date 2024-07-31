import sys
input = sys.stdin.readline
from itertools import combinations

if __name__ == '__main__':
    n, m = map(int, input().split())
    numlist = [i for i in range(1, n+1)]
    
    for seq in combinations(numlist, m):
        print(*seq)