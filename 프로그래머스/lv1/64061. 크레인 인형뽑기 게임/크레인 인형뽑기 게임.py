def solution(board, moves):
    answer = 0
    st = []
    dic = {}
    lee = len(board[0])

    for i in board:
        for j,v in enumerate(i):
            if v == 0:
                pass
            elif dic.get(j+1) is None:
                dic[j+1] = [v]
            else:
                dic[j+1].append(v)

    for i in moves:
        if len(dic[i]) >= 1:
            inin = dic[i].pop(0)
            if len(st) == 0 or st[-1] != inin:
                st.append(inin)
            elif st[-1] == inin:
                answer += 2
                st.pop()

    return answer