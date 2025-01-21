import sys

#'-'를 기준으로 나눠서 입력받기
formula = sys.stdin.readline().strip().split('-')

result = []
#나눈 입력값중에서 '+'부분은 연산해주기
for i in formula:
    sum = 0
    tmp = i.split('+')
    for j in tmp:
        sum += int(j)
    result.append(sum)
#맨처음값에다가 각각의 +한값을 빼주면 최소값
first = result[0]
for i in range(1, len(result)):
    first -= result[i]
print(first)