def solution(brown, yellow):
    answer = []
    y, x = divisor(yellow)[(brown-4)/2]
    answer.append(x+2)
    answer.append(y+2)
    return answer

def divisor(n):
    res = {}
    for i in range(1, int(n**(1/2)) + 1):
        if n % i == 0:
            a = i
            if i <= n // i:
                b = n // i
        res[a + b] = (a, b)
    return res