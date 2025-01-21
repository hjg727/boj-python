T = int(input())

def right(direct):
    return (direct+1) % 4

def check(x, y, field, N):
    return 0<=x<N and 0<=y<N and field[x][y] == 0

for test_case in range(1, T+1):
    N = int(input())
    
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    num = 1
    direct = 0

    x, y = 0, 0

    snale = [[0] * N for _ in range(N)]
    snale[x][y] = num
    
    while num < N*N:# 어떻게 나갈지 고민하기 점점 증가 혹은 감소하는 숫자 찾기

        nx = x + dx[direct]
        ny = y + dy[direct]
        
        if check(nx, ny, snale, N):
            x, y = nx, ny
            num += 1
            snale[x][y] = num
        else:
            direct = right(direct)
        
    print(f"#{test_case}")
    for row in snale:
        print(" ".join(map(str, row)))