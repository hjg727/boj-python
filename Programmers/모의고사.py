def solution(answers):
    answer = []
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    for i in range(len(answers)):
        if answers[i%len(one)] == one[i]: score[0] += 1
        if answers[i%len(two)] == two[i]: score[1] += 1
        if answers[i%len(three)] == three[i]: score[2] += 1
    
    max_score = max(score)

    if score[0] == max_score: answer.append(1)
    if score[1] == max_score: answer.append(2)
    if score[2] == max_score: answer.append(3)
    
    return answer

answers = [1,2,3,4,5]
ans = solution(answers)
print(ans)