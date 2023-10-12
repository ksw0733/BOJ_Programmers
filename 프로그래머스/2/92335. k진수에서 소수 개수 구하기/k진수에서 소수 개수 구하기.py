def convert(n, k):
    rev_base = ''
    
    while n > 0:
        n, mod = divmod(n, k)
        rev_base += str(mod)
        
    return rev_base[::-1]

def is_prime(n):
    if n == 1:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
        
    return True

def solution(n, k):
    answer = 0
    
    num = convert(n, k)
    lst = num.split('0')
    
    for n in lst:
        if not n:
            continue
            
        if is_prime(int(n)):
            answer += 1
    
    return answer