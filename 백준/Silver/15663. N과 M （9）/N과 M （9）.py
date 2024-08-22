import sys
input = sys.stdin.readline
sys.setrecursionlimit = 100000

def back_tracking(N, M, num_list, path, result, visited):
    if len(path) == M:
        result.append(path[:])
        return
    
    prev_num = None
    for i in range(N):
        if not visited[i] and num_list[i] != prev_num:
            visited[i] = True
            path.append(num_list[i])
            back_tracking(N, M, num_list, path, result, visited)
            path.pop()
            visited[i] = False
            prev_num = num_list[i]

def solution():
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))
    num_list.sort()
    visited = [False] * N
    result = []
    
    back_tracking(N, M, num_list, [], result, visited)
    
    for seq in result:
        print(" ".join(map(str, seq)))

if __name__ == '__main__':
    solution()