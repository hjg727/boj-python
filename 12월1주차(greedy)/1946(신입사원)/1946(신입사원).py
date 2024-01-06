import sys
input = sys.stdin.readline

t = int(input())

result = []

for _ in range(t):
    n = int(input())
    score = [] * n

    for _ in range(n):
        a,b = map(int, input().split())
        score.append((a,b))
    
    score.sort()
    
    count = 1
    start_score = score[0]
    for i in range(1, n):
        if score[i][0] < start_score[0] or score[i][1] < start_score[1]:
            start_score = score[i]
            count += 1
    
    result.append(count)

for i in range(len(result)):
    print(result[i])