N = int(input())
day = [0] * (N+1)
money = [0] * (N+1)

for i in range(N):
    day[i], money[i] = map(int, input().split())

dp = [0] * (N+1)

for i in range(N-1, -1, -1):
    if day[i] + i > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(money[i] + dp[i+day[i]], dp[i+1])

print(dp[0])