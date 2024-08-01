import sys
input = sys.stdin.readline
sys.setrecursionlimit = 1000000

def back_tracking(n, m, x, path):
    if len(path) == m:
        print(*path)
        return
    
    for i in range(x, n + 1):
        path.append(i)
        back_tracking(n, m, i, path)
        path.pop()
        

if __name__ == '__main__':
    n, m = map(int, input().split())
    back_tracking(n, m, 1, [])