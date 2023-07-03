def solution(n):
    answer = 0
    x = n ** (1/2)
    if x == int(x):
        return (x + 1) ** 2
    return -1