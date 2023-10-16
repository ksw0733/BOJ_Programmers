def bfs(graph, q):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    for c in q:
        queue = [[c[0], c[1], 0]]
        visited = [[False]*5 for i in range(5)]
        visited[c[0]][c[1]] = True
        
        while queue:           
            tmp = queue.pop()
            for i in range(4):
                nx = dx[i] + tmp[0]
                ny = dy[i] + tmp[1]
                if nx < 0 or nx >= 5 or ny < 0 or ny >= 5 or graph[nx][ny] == "X" or visited[nx][ny]:
                    continue
                    
                if graph[nx][ny] == "P" and tmp[2] <= 1:
                    return False
                
                if graph[nx][ny] == "O":
                    queue.append([nx,ny,tmp[2] + 1])
                    visited[nx][ny] = True
        
    return True
    

def solution(places):
    answer = []
    for place in places:
        q = []
        for i, row in enumerate(place):
            for j in range(len(place)):
                if row[j] == 'P':
                    q.append([i, j])
                    
        if len(q) == 0:
            answer.append(1)
            continue
            
        if bfs(place, q):
            answer.append(1)
            continue

        answer.append(0)
            
    return answer