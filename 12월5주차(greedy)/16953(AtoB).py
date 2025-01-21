A, B = map(int, input().split())
count = 0
while A != B:
    if B % 2 == 0:
        B = B // 2
        count += 1
    elif B % 10 == 1:
        B = int(str(B)[:-1])
        if B > A:
            count += 1
        else:
            count = -1
            break
    else:
        count = -1
        break
if A == B:
    print(count+1)
else:
    print(count)