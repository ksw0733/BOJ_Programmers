def solution(participant, completion):
    dic = {}
    sumHash = 0
    
    # hash() 함수를 이용해 key 값을 임의로 생성한 후 선수의 이름을 value로 사용
    for part in participant:
        dic[hash(part)] = part
        sumHash += hash(part)
    
    for comp in completion:
        sumHash -= hash(comp)

    return dic[sumHash]