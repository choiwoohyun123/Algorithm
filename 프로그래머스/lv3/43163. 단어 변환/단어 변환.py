from collections import deque

def solution(begin, target, words):

    if target not in words:
        return 0
    
    q = deque([(begin, 0)])
    
    while q:
        current, count = q.popleft()
        
        if current == target:
            return count
        
        for word in words:
            diff_count = 0
            for letter1, letter2 in zip(current, word):
                if letter1 != letter2:
                    diff_count += 1
            if diff_count == 1:
                q.append((word, count + 1))
                words.remove(word)
    return 0