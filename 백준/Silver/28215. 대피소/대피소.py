from itertools import combinations
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

co_li = []
index_li = []

answer = float('inf')

for _ in range(n):
  co_li.append(list(map(int, input().split())))
  
for i in range(n):
  index_li.append(i)
  
for shelters in combinations(co_li, k):
  houses = []
  distances = []
  for co in co_li:
    if co not in shelters:
      houses.append(co)
  for house in houses:
    shel_di = float('inf')
    for shelter in shelters:
      temp = abs(shelter[0] - house[0]) + abs(shelter[1] - house[1])
      shel_di = min(temp, shel_di)
    
    distances.append(shel_di)
  
  answer = min(max(distances), answer)
      
  
print(answer)
  
    