import re
from collections import Counter

def solution(str1, str2):
    answer = 0
    r = re.compile('^[^a-zA-Z]+')
    str1 = [str1.lower()[i:i+2] for i in range(0, len(str1) - 1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
    str2 = [str2.lower()[i:i+2] for i in range(0, len(str2) - 1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]
    
    
    if len(str1) == 0 and len(str2) == 0:
        return 65536
        
    c1 = Counter(str1)
    c2 = Counter(str2)
    answer = int(float(sum((c1 & c2).values())) / float(sum((c1 | c2).values())) * 65536)
        
    return answer