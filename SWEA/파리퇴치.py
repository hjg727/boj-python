T = int(input())

def sum_flies(x, y, M, field):
    sum = 0
    for i in range(x-M, x):
        for j in range(y-M, y):
            sum += field[i][j]
            """
            여기서는 들어온 좌표부터 시작해서 (M-1,M-1)까지 합을 구해야되는데
            들어온좌표가 오른쪽 제일밑인 마지막점이라생각하고 M*M범위를 생각하며 더하고있다.
            """
            
    return sum

for test_case in range(1, T+1):
    
    N, M = map(int, input().split())
    field = [[0] * N for _ in range(N)]
    
    for i in range(N):
        field[i] = list(map(int, input().split()))
    res = 0
    for i in range(N+M-1):
        for j in range(M, N):
            """
            지금 나는 (M,M)부터 (N-1, N-1)까지 탐색하고있다 이는 시작점이 0,0부터시작하지 않아서
            옳지 못한 탐색 방법이다.
            """
            x = sum_flies(i, j, M, field)
            
            if res < x:
                res = x

    print(f"#{test_case} {res}")