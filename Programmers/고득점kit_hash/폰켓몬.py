"""import itertools

def solution(nums):
    len_n = len(nums)

    poket = set(nums)
    print(poket)
    ans = list(itertools.combinations(poket, len_n//2))
    result = ans[0]
    print(len(result))

solution([3,1,2,3])
solution([3,3,3,2,2,4])
solution([3,3,3,2,2,2])"""

# import itertools
# def solution(nums):
#     ans = list(itertools.combinations(nums, len(nums)//2))
#     print(ans)

# solution([3,1,2,3])
# solution([3,3,3,2,2,4])
# solution([3,3,3,2,2,2])

def solution(nums):
    answer = len(set(nums))
    if answer > len(nums)//2:
        return len(nums)//2
    return answer
print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))
