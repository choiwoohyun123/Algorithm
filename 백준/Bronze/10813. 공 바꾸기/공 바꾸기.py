import sys
input = sys.stdin.readline
n, m = map(int, input().split())

bucket = []
for i in range(1, n + 1):
  bucket.append(i)
for _ in range(m):
  i, j = map(int, input().split())
  bucket[i-1], bucket[j-1] = bucket[j-1], bucket[i-1]
  
print(*bucket)