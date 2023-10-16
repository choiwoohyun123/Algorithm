from itertools import permutations

def solution(k, dungeons):
    k_temp = k
    result_li = []
    for dungeon_case in permutations(dungeons, len(dungeons)):
        k = k_temp
        result = 0
        check = True
        for dungeon in dungeon_case:
            if k >= dungeon[0]:
                k -= dungeon[1]
                result += 1
        result_li.append(result)
        
    
    return max(result_li)