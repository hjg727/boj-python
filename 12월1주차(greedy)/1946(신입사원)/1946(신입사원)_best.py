import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    score = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: x[0])
    count = 1
    max_interview_score = score[0][1]

    for i in range(1, n):
        if score[i][1] < max_interview_score:
            max_interview_score = score[i][1]
            count += 1
    print(count)