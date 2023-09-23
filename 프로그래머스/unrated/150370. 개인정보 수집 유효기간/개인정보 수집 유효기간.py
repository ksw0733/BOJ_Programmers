def solution(today, terms, privacies):
    answer = []
    dict_terms = {}
    
    today_y, today_m, today_d = map(int, today.split('.'))
    
    for terms in terms:
        term, period = terms.split(' ')
        dict_terms[term] = int(period)
        
    for idx, privacy in enumerate(privacies):
        date, term = privacy.split(' ')
        contract_y, contract_m, contract_d = map(int, date.split('.'))
        
        end_y = contract_y
        end_m = contract_m + dict_terms[term]
        end_d = contract_d - 1
        
        while end_m > 12:
            end_y += 1
            end_m -= 12
        
        if end_d == 0:
            end_m -= 1
            if end_m < 1:
                end_y -= 1
                end_m = 12
            end_d = 28
            
        if today_y > end_y:
            answer.append(idx + 1)
        
        if today_y == end_y and today_m > end_m:
            answer.append(idx + 1)
            
        if today_y == end_y and today_m == end_m and today_d > end_d:
            answer.append(idx + 1)
    
    return answer