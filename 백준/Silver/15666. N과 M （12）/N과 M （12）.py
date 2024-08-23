import sys
input = sys.stdin.readline
sys.setrecursionlimit = 100000

def back_tracking(N, M, num_list, path, start):
    if len(path) == M:
        print(" ".join(map(str, path)))
        return
    
    prev_num = None
    for i in range(start, N):
        if  prev_num != num_list[i]:
            path.append(num_list[i])
            back_tracking(N, M, num_list, path, i)
            path.pop()
            prev_num = num_list[i]


def solution():
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))
    num_list.sort()
    
    back_tracking(N, M, num_list, [], 0)

if __name__ == '__main__':
    solution()