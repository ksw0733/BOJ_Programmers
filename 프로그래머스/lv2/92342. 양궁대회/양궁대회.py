from itertools import combinations_with_replacement

def solution(n, info):
    answer = [-1]
    maxGap = -1e9
    candidates = list(combinations_with_replacement(range(0, 11), n))

    for candidate in candidates:
        info2 = [0] * 11
        apeach, lion = 0, 0

        for score in candidate:
            info2[10 - score] += 1

        for score, (a, l) in enumerate(zip(info, info2)):
            if a == l == 0:
                continue
            elif a >= l:
                apeach += (10 - score)
            else:
                lion += (10 - score)

        if lion > apeach:
            gap = lion - apeach
            
            if gap > maxGap:
                maxGap = gap
                answer = info2

    return answer