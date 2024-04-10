def solution(n, left, right):
    arr = []
    
#     for i in range(n):
#         for j in range(n):
#             if i == j:
#                 arr.append(i+1)
#             elif j > i:
#                 arr.append(j+1)
#             elif j < i:
#                 arr.append(i+1)

    for i in range(left, right + 1):
        a = i // n + 1
        b = i % n + 1
        arr.append(max(a,b))

    
    return arr