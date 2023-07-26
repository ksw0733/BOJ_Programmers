def solution(n):

    res = [0] * (n + 2)
    res[1], res[2] = 1, 2


    for i in range(3, n + 1):
        res[i] = res[i-1] + res[i-2]

    answer = res[n] % 1234567

    return answer