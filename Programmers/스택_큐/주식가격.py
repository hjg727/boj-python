prices = [1, 2, 3, 2, 3]

"""
def solution(prices):
    len_p = len(prices)
    answer = []
    for i in range(len_p):
        cnt = 0
        for j in range(i+1, len_p):
            if i == len_p-1:
                break
            if prices[i] <= prices[j]:
                cnt += 1
        answer.append(cnt)

    return answer
"""

def solution(prices):
    len_p = len(prices)
    answer = []
    for i in range(len_p):
        if i == len_p-1:
            answer.append(0)
        for j in range(i+1, len_p):
            if prices[i] > prices[j] or j+1==len_p:
                answer.append(j-i)
                break
            

    return answer

print(solution(prices))