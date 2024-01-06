import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * N

num = list(map(int, input().split()))

dp[0] = num[0]
for i in range(1, N):
    dp[i] = max(dp[i-1] + num[i], num[i])

print(max(dp))
'''
dp[i] = max(dp[i-1] + a[i], a[i])는
이번에 해당하는 수 까지의 모아온 합의 시작점과
그냥 이번에 해당 수의 값으로 시작하는 시작점중
더 값이 높은 시작점에서 시작하기
'''