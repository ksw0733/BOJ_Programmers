import sys
import copy

input = sys.stdin.readline

def dust(room):
    next_room = copy.deepcopy(room)
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(R):
        for j in range(C):
            if room[i][j] < 5:
                continue
            elif room[i][j] >= 5:
                tmp = room[i][j] // 5
                for k in range(4):
                    nx = j + dx[k]
                    ny = i + dy[k]
                    if 0 <= nx < C and 0 <= ny < R and room[ny][nx] != -1:
                        next_room[ny][nx] += tmp
                        next_room[i][j] -= tmp
                        
    return next_room

def clean_air_up(room, y, x):
    next_dust = copy.deepcopy(room)
    room[y][x] = 0
    
    for i in range(C - 1):
        next_dust[0][i] = room[0][i + 1]
        
    for i in range(y):
        next_dust[i][-1] = room[i + 1][-1]
    
    for i in range(C - 1):
        next_dust[y][i + 1] = room[y][i]
        
    for i in range(y):
        next_dust[i + 1][0] = room[i][0]
        
    next_dust[y][x] = -1
    
    return next_dust

def clean_air_down(room, y, x):
    next_dust = copy.deepcopy(room)
    room[y][x] = 0
    
    for i in range(C - 1):
        next_dust[-1][i] = room[-1][i + 1]
        
    for i in range(y, R - 1):
        next_dust[i + 1][-1] = room[i][-1]
    
    for i in range(C - 1):
        next_dust[y][i + 1] = room[y][i]
        
    for i in range(y, R - 1):
        next_dust[i][0] = room[i + 1][0]
        
    next_dust[y][x] = -1
    
    return next_dust


if __name__ == "__main__":
    R, C, T = map(int, input().split())
    room = [list(map(int, input().split())) for _ in range(R)]
    for r in range(R):
        if -1 in room[r]:
            y1, x1 = r, room[r].index(-1)
            y2, x2 = r + 1, x1
            break
    
    for _ in range(T):
        room = dust(room)
        room = clean_air_up(room, y1, x1)
        room = clean_air_down(room, y2, x2)
    
    res = 0
    for i in range(R):
        res += sum(room[i])
        
    print(res + 2)