def solution(tickets):
    answer = []
    routes = {}

    for a, b in tickets:
        routes[a] = routes.get(a, []) + [b] # get을 이용해 default값 설정 가능

    for a in routes:
        routes[a].sort(reverse=True)

    start = ['ICN']

    while start:
        top = start[-1]
        if not top in routes or not routes[top]: # 현재 top 출발 도시에서 갈 수 있는 도착 도시가 없는 경우를 체크
            answer.append(start.pop())
        else:                                    # 출발 도시에서 갈 수 있는 도착 도시가 있는 경우
            start.append(routes[top].pop()) 

    return answer[::-1]