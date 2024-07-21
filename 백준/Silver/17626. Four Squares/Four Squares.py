import sys
input = sys.stdin.readline

def solution(n):
    sq = [0 if i**0.5%1 else 1 for i in range(n+1)]
    
    mincount = 4
    for i in range(int(n**0.5), 0, -1):
        if sq[n] :
            mincount=1
            break
        elif sq[n-i**2] :
            mincount=2
            break
        else:
            for j in range(int((n-i**2)**0.5), 0, -1):
                if sq[(n-i**2)-j**2]:
                    mincount=3
                    
    return mincount

if __name__ == '__main__':
    n = int(input())
    print(solution(n))