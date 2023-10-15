def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key = lambda x: (x[col - 1], -x[0]))
    
    s_n = []
    for i in range(row_begin - 1, row_end):
        tmp = 0
        for j in range(len(data[0])):
            tmp += data[i][j] % (i + 1)
        s_n.append(tmp)
        
    for i in range(len(s_n)):
        answer ^= s_n[i]
        
    return answer