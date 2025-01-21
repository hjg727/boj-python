N = int(input())
clap = []
for x in range(1, N+1):
    x = str(x)

    cnt = x.count('3') + x.count('6') + x.count('9')

    if cnt > 0:
        clap.append('-'*cnt)
    else:
        clap.append(x)
print(" ".join(clap))