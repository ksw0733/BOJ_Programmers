import sys
import math
input = sys.stdin.readline

def solution(A, B, C):
    result = 0
    for num in A:
        if num <= B:
            result += 1
        else:
            num -= B
            result += 1
            cnt = math.ceil(num/C)
            result += cnt
            
    return result

class_num = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
print(solution(A, B, C))