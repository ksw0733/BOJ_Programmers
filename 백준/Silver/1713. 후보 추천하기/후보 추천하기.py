import sys
input = sys.stdin.readline

def solution(lst):
    photo = {}
    for i in range(vote):
        if lst[i] in photo:
            photo[lst[i]][0] += 1
        else:
            if len(photo) < N:
                photo[lst[i]] = [1, i]
            else:
                del_list = sorted(photo.items(), key = lambda x: (x[1][0], x[1][1]))
                del_key = del_list[0][0]
                del(photo[del_key])
                photo[lst[i]] = [1, i]
    
    return list(map(str,sorted(photo.keys())))
            

if __name__ == "__main__":
    N = int(input())
    vote = int(input())
    lst = list(map(int, input().split()))
    ans = solution(lst)
    print(' '.join(ans))