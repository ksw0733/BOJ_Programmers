def solution(msg):
    answer = []
    dic = {}
    num = 1
    for code in range(65,91):
        dic[chr(code)] = num
        num += 1
    
    while True:
        i = 0
        
        if msg in dic:
            answer.append(dic[msg])
            return answer
        
        else:
            for j in range(1, len(msg) + 1):
                if msg[i:j] not in dic:
                    answer.append(dic[msg[i:j-1]])
                    dic[msg[i:j]] = num
                    num += 1
                    
                    msg = msg[j-1:]
                    break

    return answer