A = [input().strip()]
B = [input().strip()]

A_length = len(A)
B_length = len(B)

dp = [[0]*(B_length+1) for _ in range(A_length+1)]
count = 0
for i in range(1, A_length+1):
    for j in range(1, B_length+1):
        if A[i-1] == B[j-1]:
            dp[i][j] == dp[i-1][j-1] + 1
        else:
            dp[i][j] == max(dp[i][j-1], dp[i-1][j])
print(dp[A_length][B_length])