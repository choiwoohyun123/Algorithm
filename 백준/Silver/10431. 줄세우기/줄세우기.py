P = int(input())



for test_case in range(1, P + 1):
  result = 0
  li = list(map(int, input().split()))[1:]
  for i in range(1, len(li)):
    for j in range(i):
      if li[j] > li[i]:
        li.insert(j, li[i])
        del li[i+1] 
        result += i - j
        break

  print(test_case, result)        

