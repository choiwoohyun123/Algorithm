def solution(brown, yellow):
    answer = [0, 0]
    w_h_sum = brown//2 + 2
    h = 3
    while(1):
        w = w_h_sum - h
        if (w - 2) * (h - 2) == yellow:
            answer[0] = w
            answer[1] = h
            break
        h += 1
        
    return answer

# import math

# def solution(brown, yellow ):
#     answer = []
#     for i in range(1, math.floor(yellow**(1/2)) + 1):
#         width = int(yellow//i)
#         height = i
#         if ((height + 2)*(width + 2)) - height * width == brown:
#             answer = [width + 2, height + 2]
#     return answer