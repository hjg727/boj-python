A, B = map(int, input().split())
count = 0
while A < B:
    if B % 2 == 0:
        B = B // 2
        count += 1
    elif B % 10 == 1:
        B = B // 10
        count += 1
    else:
        break
if A == B:
    print(count+1)
else:
    print(-1)