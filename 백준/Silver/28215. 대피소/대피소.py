from itertools import combinations
import sys

input = sys.stdin.read
data = input().split()

n, k = int(data[0]), int(data[1])
co_li = [(int(data[i*2+2]), int(data[i*2+3])) for i in range(n)]

answer = float('inf')

for shelters in combinations(co_li, k):
    max_min_dist = 0
    for house in co_li:
        if house in shelters:
            continue
        min_dist = min(abs(shelter[0] - house[0]) + abs(shelter[1] - house[1]) for shelter in shelters)
        max_min_dist = max(max_min_dist, min_dist)
    answer = min(answer, max_min_dist)

print(answer)
