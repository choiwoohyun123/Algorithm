import copy
from collections import deque

def solution(game_board, table):
    n = len(game_board)
    answer = 0

    blank = []
    for i in range(n):
        for j in range(n):
            if game_board[i][j] == 0:
                blank.append(bfs(game_board, i, j, [0, 0], n, 0))

    for k in range(4):
        table = rotate(table)
        copy_table = copy.deepcopy(table)
        for i in range(n):
            for j in range(n):
                if copy_table[i][j] == 1:
                    block = bfs(copy_table, i, j, [0, 0], n, 1)
                    if block in blank:
                        blank.remove(block)
                        answer += len(block)
                        table = copy.deepcopy(copy_table)
                    else:
                        copy_table = copy.deepcopy(table)
    return answer

def bfs(board, x, y, position, n, num):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    q = deque([(x, y, position)])
    board[x][y] = 2  # 방문처리
    result = [position]

    while q:
        x, y, position = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == num:
                q.append((nx, ny, [position[0] + dx[i], position[1] + dy[i]]))
                board[nx][ny] = 2  # 방문처리
                result.append([position[0] + dx[i], position[1] + dy[i]])
                
    return result

def rotate(table):
    n = len(table)
    rotated = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            rotated[j][n - i - 1] = table[i][j]

    return rotated