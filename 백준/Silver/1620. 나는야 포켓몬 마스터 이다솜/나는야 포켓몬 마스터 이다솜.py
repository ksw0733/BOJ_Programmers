import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())
    poket_dic = {}
    for i in range(1, n+1):
        poketmon = str(input().rstrip())
        poket_dic[i] = poketmon
    poket_dic2 = {v:k for k,v in poket_dic.items()}
    
    for _ in range(m):
        order = input().rstrip()
        if order.isnumeric():
            order = int(order)
            print(poket_dic[order])
        else:
            print(poket_dic2[order])