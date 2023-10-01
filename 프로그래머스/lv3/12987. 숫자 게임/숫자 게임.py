def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    j = 0
    
    for a in A:
        while j < len(B):
            if a < B[j]:  # A의 원소가 B의 원소보다 작은 경우
                answer += 1
                j += 1
                break
            j += 1

    return answer