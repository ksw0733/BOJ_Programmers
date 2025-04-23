import sys
from collections import defaultdict
input = sys.stdin.readline

def solution(students):
    cls = [[0] * N for _ in range(N)]
    
    for student in students:
        tmp = []
        for j in range(N):
            for i in range(N):
                if cls[j][i] == 0:
                    like, empty = 0, 0
                    
                    for k in range(4):
                        nx = i + dx[k]
                        ny = j + dy[k]
                        
                        if 0 <= nx < N and 0 <= ny < N:
                            if cls[ny][nx] in student[1:]:
                                like += 1
                                
                            if cls[ny][nx] == 0:
                                empty += 1
                    tmp.append((j, i, like, empty))
        tmp.sort(key = lambda x: (-x[2], -x[3], x[0], x[1]))
        cls[tmp[0][0]][tmp[0][1]] = student[0]
        
    return cls

if __name__ == "__main__":
    N = int(input())
    students = [list(map(int, input().split())) for _ in range(N ** 2)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    ans = 0
    score = [0, 1, 10, 100, 1000]
    
    res = solution(students)
    students.sort()
    
    for j in range(N):
        for i in range(N):
            cnt = 0
            
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                
                if 0 <= nx < N and 0 <= ny < N:
                    if res[ny][nx] in students[res[j][i] - 1]:
                        cnt += 1
            
            ans += score[cnt]
    
    print(ans)