import numpy as np

def solution(arr1, arr2):
    
    a = np.array(arr1)
    b = np.array(arr2)
    answer = a.dot(b)
    
    return answer.tolist()