def solution(n, t, m, p):
    answer = ''
    num = ''
    
    for i in range(t * m):
        num += str(convert_notation(i, n))
        
    for j in range(p-1, len(num), m):
        answer += num[j]
        if len(answer) == t:
            break
            
    return answer

def convert_notation(n, base):
    T = '0123456789ABCDEF'
    q, r = divmod(n, base)
    
    return convert_notation(q, base) + T[r] if q else T[r]