def solution(s):
    answer = 0
    
    for i in range(len(s)):
        stack = []
        for j in range(i, len(s)):
            if stack:
                if stack[-1] == "[" and s[j] == "]":
                    stack.pop()
                elif stack[-1] == "{" and s[j] == "}":
                    stack.pop()
                elif stack[-1] == "(" and s[j] == ")":
                    stack.pop()
                else:
                    stack.append(s[j])
            else:
                stack.append(s[j])
        if not stack:
            answer += 1
        s += s[i]
    print(answer)
    return answer