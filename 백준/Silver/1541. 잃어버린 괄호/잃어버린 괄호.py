import sys
input = sys.stdin.readline

def solution(expression):
    tmp = []
    for i in expression:
        cnt = 0
        for j in i.split('+'):
            cnt += int(j)
        tmp.append(cnt)
    result = tmp[0]
    for i in tmp[1:]:
        result -= i
    return result
                
if __name__ == "__main__":
    expression = input().rstrip().split('-')
    print(solution(expression))