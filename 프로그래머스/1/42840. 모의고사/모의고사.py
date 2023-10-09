def solution(answers):
    answer = []
    person = [0]*3
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]
    for i in range(len(answers)):
        if answers[i] == p1[i%5]:
            person[0] += 1
        if answers[i] == p2[i%8]:
            person[1] += 1
        if answers[i] == p3[i%10]:
            person[2] += 1

    winner = max(person)
    for i in range(len(person)):
        if person[i] == winner:
            answer.append(i+1)
    return answer