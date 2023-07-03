def solution(left, right):
    answer = 0
    for num in range(left, right + 1):
        if divisor(num) % 2 == 0:
            answer += num
        else:
            answer -= num
    return answer

def divisor(n):
    res = []
    for i in range(1, int(n**(1/2)) + 1):
        if n % i == 0:
            res.append(i)
            if i < n // i:
                res.append(n // i)
    return len(res)
    