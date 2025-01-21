T = int(input())

def sum_cnt(x, y, M, field):
    hap = 0
    for i in range(x, x+M):
        for j in range(y, y+M):
            hap += field[i][j]
    return hap

for test_case in range(1, T+1):

    N, M = map(int, input().split())
    field = [[0] * N for _ in range(N)]
    for i in range(N):
        field[i] = list(map(int, input().split()))

    res = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            v = sum_cnt(i, j, M, field)
            if res < v:
                res = v
    
    print(f"#{test_case} {res}")