import sys
from collections import defaultdict
from math import ceil
input = sys.stdin.readline

def solution(num):
    dic = defaultdict(int)
    
    for i in num:
        dic[i] += 1
    dic['6'] = ceil((dic['6'] + dic['9']) / 2)
    dic['9'] = dic['6']
    return print(max(dic.values()))
        

if __name__ == '__main__':
    num = str(input().rstrip())
    solution(num)