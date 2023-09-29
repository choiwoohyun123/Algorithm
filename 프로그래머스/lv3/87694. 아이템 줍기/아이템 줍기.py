from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    
    graph = [[-1] * 102 for i in range(102)]
    
    for r in rectangle:
      x1, y1, x2, y2 = map(lambda x: x*2, r)
      for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
          if x1 < i < x2 and y1 < j < y2:
            graph[i][j] = 0
          elif graph[i][j] != 0:
            graph[i][j] = 1
    
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    q = deque([(characterX * 2, characterY * 2)])
    visited = [[False] * 102 for i in range(102)]
    visited[characterX * 2][characterY * 2] = True
    graph[characterX * 2][characterY * 2] = 0

    
    while q:
      x, y = q.popleft()
      if x == itemX * 2 and y == itemY * 2:
        answer = graph[x][y] // 2
        break
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if graph[nx][ny] == 1 and visited[nx][ny] == False:
          q.append((nx, ny))
          visited[nx][ny] = True
          graph[nx][ny] = graph[x][y] + 1
          
            
    
    
    return answer
  
print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]],1,3,7,8))