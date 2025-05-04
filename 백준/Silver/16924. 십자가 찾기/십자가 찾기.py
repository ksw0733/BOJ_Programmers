n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]

result = []

visited = [[0] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(m):
        if board[i][j] == '*':
            length = 0
            while True:
                flag = True
                for d in range(4):
                    nx = i + dx[d] * (length + 1)
                    ny = j + dy[d] * (length + 1)
                    if nx < 0 or nx >= n or ny < 0 or ny >= m or board[nx][ny] != '*':
                        flag = False
                        break
                if flag:
                    length += 1
                else:
                    break

            if length > 0:
                result.append((i + 1, j + 1, length))  # 1-based index
                visited[i][j] = 1
                for l in range(1, length + 1):
                    for d in range(4):
                        nx = i + dx[d] * l
                        ny = j + dy[d] * l
                        visited[nx][ny] = 1

for i in range(n):
    for j in range(m):
        if board[i][j] == '*' and visited[i][j] == 0:
            print(-1)
            exit()

print(len(result))
for x, y, l in result:
    print(x, y, l)
