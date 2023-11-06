def choose(a, b, dic):
    if dic[a] >= dic[b]:
        return a
    else:
        return b

def solution(survey, choices):
    answer = ''
    dic = {"R": 0, "T": 0,
           "C": 0, "F": 0,
           "J": 0, "M": 0,
           "A": 0, "N": 0}
    for s, choice in zip(survey, choices):
        if choice <= 3:
            dic[s[0]] += 4 - choice
        elif choice >= 5:
            dic[s[1]] += choice - 4
            
    answer += choose("R", "T", dic)
    answer += choose("C", "F", dic)
    answer += choose("J", "M", dic)
    answer += choose("A", "N", dic)
     
    return answer