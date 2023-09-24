def fib(n):
    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    fibo = [0] * (n + 1)
    fibo[1] = 1
    
    for i in range(2, n + 1):
        fibo[i] = fibo[i - 2] + fibo[i - 1]
    
    return fibo[n]

def solution(n):
    answer = fib(n) % 1234567
    
    return answer