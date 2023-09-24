def solution(players, callings):
    answer = []
    dic_1 = {}
    dic_2 = {}
    
    for idx, player in enumerate(players):
        dic_1[player] = idx + 1
        dic_2[idx + 1] = player
        
    for calling in callings:
        now = dic_1[calling]
        new = dic_1[calling] - 1
        player = dic_2[new]
        
        dic_2[new], dic_2[now] = calling, player
        dic_1[calling], dic_1[player] = new, now
    
    answer = [v for _, v in sorted(dic_2.items())]
    
    return answer