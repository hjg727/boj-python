def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

"""def solution(numbers):
    answer = 0
    ans = set()
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            ans.add(int(numbers[i:j+1]))

    numbers = numbers[::-1]
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            ans.add(int(numbers[i:j+1]))
    if 1 in ans:
        ans.remove(1)
    print(ans)
    for a in ans:
        
        i = 2
        
        while(i <= a**(1/2)):
            if a % i == 0:
                ans.remove(a)
                break
            i += 1
        answer += 1
    
    return answer

print(solution("011"))
"""
import itertools
def solution(numbers):
    ans = set()

    # 모든 가능한 순열을 생성하여 숫자로 변환
    for length in range(1, len(numbers) + 1):
        for perm in itertools.permutations(numbers, length):
            num = int("".join(perm))
            ans.add(num)

    if 0 in ans:
        ans.remove(0)

    if 1 in ans:
        ans.remove(1)

    # 소수 개수 세기
    answer = sum(1 for num in ans if is_prime(num))

    return answer
print(solution("17"))