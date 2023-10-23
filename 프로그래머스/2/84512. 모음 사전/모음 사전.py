from itertools import product

def solution(word):
    li = []
    for i in range(1, 6):
        for j in product("AEIOU", repeat = i):
            j = "".join(j)
            li.append(j)
    li.sort()
    return li.index(word) + 1