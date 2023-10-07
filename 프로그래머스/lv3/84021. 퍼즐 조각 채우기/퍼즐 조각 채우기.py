import copy
from collections import deque



def solution(game_board, table):
    n = len(game_board)
    answer = 0
    
    blank = []

    for i in range(n):
        for j in range(n):
            if game_board[i][j] == 0:
                blank.append(bfs(game_board, i, j, n, 0))
                
    for k in range(4):
        table = rotate(table)
        copy_table = copy.deepcopy(table)
        for i in range(n):
            for j in range(n):
                if copy_table[i][j] == 1:
                    block = bfs(copy_table, i, j, n, 1)
                    if block in blank:
                        blank.remove(block)
                        answer += len(block)
                        table = copy.deepcopy(copy_table)
                    else:
                        copy_table = copy.deepcopy(table)
    return answer
    
def bfs(graph, x, y, n, num):
    q = deque([(x, y, [0, 0])])
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    graph[x][y] = 2
    result = [[0, 0]]
    
    while q:
        x, y, position = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == num:
                graph[nx][ny] = 2
                q.append((nx, ny, [position[0] + dx[i], position[1] + dy[i]]))
                result.append([position[0] + dx[i], position[1] + dy[i]])
                
    return result
            
    
def rotate(table):
    n = len(table)
    rotate_table = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotate_table[i][j] = table[j][n - i - 1]
    
    return rotate_table