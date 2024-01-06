import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    N, M = map(int, input().split())
    dp = [[0 for _ in range(M+1)] for _ in range(N+1)]
    for i in range(M+1):
        dp[1][i] = i
    for i in range(2, N+1):#i가 1이면 이중for문 실행안된다.
        #(이유. start가 end보다 크거나같은경우, 빈리스트 반환이므로 실행 되지않는다.)
        for j in range(i, M+1):
            dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
    print(dp[N][M])
# jCi(동쪽 사이트 j개 중에서 서쪽 사이트 i개를 선택하는 방법의 수)
