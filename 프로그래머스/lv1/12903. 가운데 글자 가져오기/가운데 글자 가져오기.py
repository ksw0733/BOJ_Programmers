def solution(s):
    answer = ''
    num = len(s)
    if num % 2 == 1:
        answer = s[num//2]
    else:
        answer = s[(num//2) - 1 : (num//2) + 1]
    return answer