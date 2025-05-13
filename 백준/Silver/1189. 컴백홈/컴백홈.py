import sys
input = sys.stdin.readline

def backtracking(x, y, count):
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    if (x, y) == (0, C - 1):
        return 1 if count == K else 0
    
    result = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < R and 0 <= ny < C and road[nx][ny] != 'T':
            road[nx][ny] = 'T'
            result += backtracking(nx, ny, count + 1)
            road[nx][ny] = '.'

    return  result

if __name__ == '__main__':
    R, C, K = map(int, input().split())
    road = [list(input().rstrip()) for _ in range(R)]
    road[R - 1][0] = 'T'
    print(backtracking(R - 1, 0, 1))