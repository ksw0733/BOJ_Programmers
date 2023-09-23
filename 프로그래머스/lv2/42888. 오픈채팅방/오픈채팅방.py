def solution(record):
    answer = []
    user = dict()
    actions = []
    
    for event in record:
        info = event.split(' ')
        command, uid = info[0], info[1]
        
        if command in ('Enter', 'Change'):
            nickname = info[2]
            user[uid] = nickname
        actions.append((command, uid))
        
    for action in actions:
        command, uid = action[0], action[1]
        if command == 'Enter':
            answer.append(f'{user[uid]}님이 들어왔습니다.')
            
        if command == 'Leave':
            answer.append(f'{user[uid]}님이 나갔습니다.')
        
    return answer