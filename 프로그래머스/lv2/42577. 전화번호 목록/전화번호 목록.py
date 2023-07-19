def solution(phone_book):
    hash_map = {}
    
    for phone_number in phone_book:
        hash_map[phone_number] = 1
        
    for phone_number in phone_book:
        tmp = ''
        
        for number in phone_number:
            tmp += number
            
            if (tmp in hash_map) and (tmp != phone_number):
                return False
            
    return True