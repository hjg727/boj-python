def solution(arr):
    tmp = None
    answer = []
    for a in arr:
        if a != tmp:
            answer.append(a)
            tmp = a
    return answer


print(solution([4,4,4,3,3]))

a = [4,4,4,3,3]
b = []
print(a[-1:])
print(a)
for i in a:
    if b[-1:] == [i]:
        print(b[-1:])
        continue
    b.append(i)

"""for i in a:
    print([i])"""