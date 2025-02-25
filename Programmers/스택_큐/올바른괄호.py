def solution(s):

    moon = []

    for i in s:
        if i == "(":
            moon.append(i)
        
        else:
            if moon:
                moon.pop()
            else:
                return False
    return len(moon) == 0

print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))