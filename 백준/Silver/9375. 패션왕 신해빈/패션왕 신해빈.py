import sys
input = sys.stdin.readline

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        dict = {}
        n = int(input())
        for _ in range(n):
            cloth, cloth_type = input().rstrip().split()
            if cloth_type in dict:
                dict[cloth_type].append(cloth)
            else:
                dict[cloth_type] = [cloth]
        cnt = 1
        
        for cloth in dict:
            cnt *= (len(dict[cloth]) + 1)
        
        print(cnt-1)