from collections import deque
import copy

def solution(n, wires):
    answer = -1
    graph = [[] for _ in range(n + 1)]
    abs_li = []
    
    
    for i in wires:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
    
    graph_temp = copy.deepcopy(graph)
    for cut_line in wires:
        visited = [False] * n
        graph = copy.deepcopy(graph_temp)
        graph[cut_line[0]].remove(cut_line[1])
        graph[cut_line[1]].remove(cut_line[0])
        
        q = deque([wires[0][0]])
        
        while q:
            s = q.popleft()
            visited[s - 1] = True
            for d in graph[s]:
                if not visited[d - 1]:
                    visited[d - 1] = True
                    q.append(d)
                    
        abs_li.append(abs(visited.count(True) - visited.count(False)))
            

        
    return min(abs_li)