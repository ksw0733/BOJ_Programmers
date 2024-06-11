import sys
input = sys.stdin.readline

def solution(n):
    one = [0] * (n+1)
    zero = [0] * (n+1)
    if n == 0:
        print(1, 0)
        return
    elif n == 1:
        print(0, 1)
        return
    else:
        zero[0], one[1] = 1, 1
        for i in range(2, n+1):
            zero[i] = one[i-1]
            one[i] = zero[i-1] + one[i-1]
        print(zero[n], one[n])
    
if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        solution(int(input()))