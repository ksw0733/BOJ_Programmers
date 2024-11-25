import sys
input = sys.stdin.readline

def GPA(lst):
    score = {
        'A+': 4.5,
        'A0': 4.0,
        'B+': 3.5,
        'B0': 3.0,
        'C+': 2.5,
        'C0': 2.0,
        'D+': 1.5,
        'D0': 1.0,
        'F': 0.0
    }
    
    credit_sum = 0
    grade_sum = 0
    
    for credit, grade in lst:
        if grade not in score:
            continue
        credit_sum += float(credit)
        grade_sum += float(credit)*score[grade]
    
    return grade_sum / credit_sum
        

if __name__ == '__main__':
    grade_list = []
    for _ in range(20):
        subject, credit, grade = input().rstrip().split(' ')
        grade_list.append((credit, grade))
        
    print(GPA(grade_list))