import sys
input = sys.stdin.readline

def solution(string):
    word_stack = []
    tag = False
    res = ''
    for s in string:
        if s == ' ':
            while word_stack:
                res += word_stack.pop()
            res += s
        
        elif s == '<':
            while word_stack:
                res += word_stack.pop()
            tag = True
            res += s
        
        elif s == '>':
            tag = False
            res += s
        
        elif tag:
            res += s
        
        else:
            word_stack.append(s)
            
    while word_stack:
        res += word_stack.pop()
            
    return res
        

if __name__ == '__main__':
    
    string = str(input().rstrip())
    print(solution(string))