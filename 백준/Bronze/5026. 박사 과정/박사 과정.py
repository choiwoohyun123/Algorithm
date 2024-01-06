n = int(input())

for _ in range(n):
  input_li = input()
  if "+" in input_li:
    input_li = list(input_li.split("+"))
    print(int(input_li[0]) + int(input_li[1]))
  else:
    input_li = list(input_li)
    print("skipped")