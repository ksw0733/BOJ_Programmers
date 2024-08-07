import sys
input = sys.stdin.readline
sys.setrecursionlimit = 1000000

def back_tracking(m, num_list, path, visited):
    if len(path) == m:
        print(*path)
        return
    
    for i in range(len(num_list)):
        if not visited[i]:
            visited[i] = True
            path.append(num_list[i])
            back_tracking(m, num_list, path, visited)
            path.pop()
            visited[i] = False
        

if __name__ == '__main__':
    n, m = map(int, input().split())
    num_list = sorted(list(map(int, input().split())))
    visited = [False] * n
    back_tracking(m, num_list, [], visited)