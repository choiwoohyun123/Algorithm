from collections import deque
import copy

def bfs(start, graph, n):
    visited = [False] * (n + 1)
    q = deque([start])
    visited[start] = True
    count = 1
    
    while q:
        current = q.popleft()
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                q.append(neighbor)
                count += 1
                
    return count

def solution(n, wires):
    answer = float('inf')
    graph = [[] for _ in range(n + 1)]
    
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    for cut_line in wires:
        graph_temp = copy.deepcopy(graph)
        graph_temp[cut_line[0]].remove(cut_line[1])
        graph_temp[cut_line[1]].remove(cut_line[0])
        
        # 첫 번째 그래프의 연결된 송전탑 개수 계산
        count1 = bfs(cut_line[0], graph_temp, n)
        # 전체 송전탑 개수에서 첫 번째 그래프의 송전탑 개수를 빼면 두 번째 그래프의 송전탑 개수가 됩니다.
        count2 = n - count1
        
        # 두 전력망의 송전탑 개수 차이 계산
        difference = abs(count1 - count2)
        answer = min(answer, difference)
            
    return answer
