N, K = map(int, input().split())
coin = []
for _ in range(N):
    coin.append(int(input()))

coin = coin[::-1]

cnt = 0

for i in coin:
    if i > K:
        continue
    else:
        cnt += K//i
        K = K % i
print(cnt)