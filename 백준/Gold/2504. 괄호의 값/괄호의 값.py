import sys
input = sys.stdin.readline

def solution(string):
    stack = []
    ans = 0
    tmp = 1
    for i in range(len(string)):
        if string[i] == '(':
            tmp *= 2
            stack.append(string[i])
            
        elif string[i] == '[':
            tmp *= 3
            stack.append(string[i])
            
        elif string[i] == ')':
            if not stack or stack[-1] =='[':
                return 0
            if string[i-1] =='(':
                ans += tmp
            stack.pop()
            tmp //= 2
        
        elif string[i] == ']':
            if not stack or stack[-1] == '(':
                return 0
            if string[i-1] == '[':
                ans += tmp
            stack.pop()
            tmp //= 3
    if stack:
        return 0
    
    return ans

if __name__ == "__main__":
    string = str(input().rstrip())
    print(solution(string))