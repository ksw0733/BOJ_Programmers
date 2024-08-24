import sys
input = sys.stdin.readline

def solution(A, B):
    answer = 0
    
    while A <= B:
        if A == B:
            return answer + 1
        
        if B % 10 == 1:
            B = B // 10
            answer += 1
            
        else:
            B = B / 2
            answer += 1
        
    return -1

if __name__ == '__main__':
    A, B = map(int, input().split())
    print(solution(A, B))