def solution(answers):
    answer = []
    person_1 = [1, 2, 3, 4, 5]
    person_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    person_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == person_1[i % 5]:
            score[0] += 1
        if answers[i] == person_2[i % 8]:
            score[1] += 1
        if answers[i] == person_3[i % 10]:
            score[2] += 1
    
    for i in range(len(score)):
        if score[i] == max(score):
            answer.append(i+1)
    
    return answer