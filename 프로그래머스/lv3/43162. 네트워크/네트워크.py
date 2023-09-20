def dfs(computers, visited , v):
    stack = [v]
    while stack:
        node = stack.pop()
        if visited[node] == False:
            visited[node] = True
        for i in range(len(computers)):
            if computers[node][i] == 1 and visited[i] == False:
                stack.append(i)

def solution(n, computers):
    answer = 0
    visited = [False] * n
    while(1):
        if False not in visited:
            break
        v = visited.index(False)
        dfs(computers, visited, v)
        answer += 1
    
    return answer