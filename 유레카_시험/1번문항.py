D = int(input())
A = list(map(int, input().split()))

bike = A[0]
answer = A[0]
for i in range(1, D):
    if bike <= A[i]:
        bike += 1
        answer += bike
    else:
        bike = A[i]
        answer += bike

print(answer)