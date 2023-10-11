from itertools import permutations

def solution(numbers):
    answer = 0
    numbers_li = []
    
    repeat_check = []
    for i in range(1, len(numbers) + 1):
        for j in permutations(numbers, i):
            prime_check = 1
            temp = int("".join(j))
            if (temp not in repeat_check) and (temp != 0 and temp != 1):
                repeat_check.append(temp)
                for k in range(2, temp):
                    if temp % k == 0:
                        prime_check = 0
                        break
                if prime_check == 1:
                    answer += 1
    return answer