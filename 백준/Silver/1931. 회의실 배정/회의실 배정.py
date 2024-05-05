import sys
input = sys.stdin.readline

def solution(n):
    meetings = []
    for _ in range(n):
        start, end = map(int, input().split())
        meetings.append((start, end))
    
    meetings.sort(key = lambda x: (x[1], x[0]))
    
    time = 0
    answer = 0
    for meeting in meetings:
        if time <= meeting[0]:
            time = meeting[1]
            answer += 1
            
    return answer
    
    
if __name__ == '__main__':
    n = int(input())
    print(solution(n))
    