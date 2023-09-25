from collections import deque

def solution(maps):

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    q = deque([(0,0)])

    while q:
        x, y = q.popleft()        
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]):
                continue
            if maps[nx][ny] == 0:
                continue
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                q.append((nx,ny))
        
    if maps[-1][-1] == 1:
        return -1
    else:
        return maps[-1][-1]