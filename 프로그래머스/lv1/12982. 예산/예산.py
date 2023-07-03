def solution(d, budget):
    answer = 0
    tmp = 0
    d.sort()
    for n in d:
        tmp += n
        if tmp <= budget:
            answer += 1
    return answer