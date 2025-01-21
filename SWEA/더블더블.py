N = int(input())
res = [1]

for i in range(1, N + 1):
    res.append(2**i)
print(" ".join(map(str, res)))