import sys
input = sys.stdin.readline

def solution(x, y, size):
    global white, blue
    color = paper[x][y]
    same_color = True
    
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != color:
                same_color = False
                break
        if not same_color:
            break
    if same_color:
        if color == 0:
            white += 1
        else:
            blue += 1
    else:
        new_size = size // 2
        solution(x, y, new_size)
        solution(x, y + new_size, new_size)
        solution(x + new_size, y, new_size)
        solution(x + new_size, y + new_size, new_size)

if __name__ == "__main__":
    n = int(input())
    paper = [list(map(int, input().split())) for _ in range(n)]
    white = 0
    blue = 0
    solution(0, 0, n)
    print(white)
    print(blue)