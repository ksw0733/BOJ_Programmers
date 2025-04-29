import sys
input = sys.stdin.readline

def solution(S, T):
    for _ in range(len(T) - len(S)):
        if T[-1] == 'A':
            T = T[:-1]
        else:
            T = T[:-1]
            T = T[::-1]
            
    return 1 if S == T else 0
        
if __name__ == "__main__":
    S = input().rstrip()
    T = input().rstrip()
    print(solution(S, T))