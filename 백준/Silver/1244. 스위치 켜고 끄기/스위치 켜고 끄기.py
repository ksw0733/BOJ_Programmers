import sys
input = sys.stdin.readline

def toggle_switch(switch, index):
    switch[index] = 1 - switch[index]

def solution(switch, order):
    for gender, num in order:
        if gender == 1:
            for i in range(num, len(switch), num):
                toggle_switch(switch, i)
        
        elif gender == 2:
            toggle_switch(switch, num)
            left, right = num-1, num+1
            while left >= 1 and right <= len(switch)-1 and switch[left] == switch[right]:
                toggle_switch(switch, left)
                toggle_switch(switch, right)
                left -= 1
                right += 1
    
    return switch
            

if __name__ == '__main__':
    n = int(input())
    switch = [0] + list(map(int, input().split()))
    m = int(input())
    order = []
    for _ in range(m):
        gender, number = map(int, input().split())
        order.append((gender, number))
    
    solution(switch, order)
    for i in range(1, n + 1):
        print(switch[i], end = ' ')
        if i % 20 == 0:
            print()