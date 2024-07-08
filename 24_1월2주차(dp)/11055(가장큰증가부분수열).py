import sys

A_length = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

dp = A[:]#dp = A 놉, 각 원소를 마지막으로 하는 부분 수열의 최대합

for i in range(A_length):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + A[i])
            #지금 나의값이맞는지, 이전까지한값의 지금을 더한값이 맞는지
            #즉, A[i] > A[j]가 여러번일때 개중 최댓값 구하기

print(max(dp))