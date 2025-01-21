T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    
    dp = [[0] * (i+1) for i in range(N)]
    dp[0][0] = 1
    
    for i in range(1, N):
        for j in range(i+1):
            if j == 0 or j == i:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
    
    print(f"#{test_case}")
    for row in dp:
        print(" ".join(map(str, row)))