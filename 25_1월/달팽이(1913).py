import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

# n x n 행렬을 0으로 초기화
matrix = [[0] * n for _ in range(n)]

# 중심 위치 (0-index 기준)
x = n // 2
y = n // 2
matrix[x][y] = 1  # 중심에 1 채우기

# 방향: [위, 오른쪽, 아래, 왼쪽]
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
d = 0  # 처음 이동 방향은 위쪽 (인덱스 0)
step = 1  # 각 방향으로 이동할 칸 수
num = 2   # 채워넣을 다음 숫자

# n*n 까지 채우기
while num <= n * n:
    # 각 step마다 두 방향으로 이동
    for _ in range(2):
        dx, dy = dirs[d]
        for _ in range(step):
            if num > n * n:
                break
            x += dx
            y += dy
            matrix[x][y] = num
            num += 1
        d = (d + 1) % 4  # 시계방향으로 다음 방향
    step += 1  # 두 방향 이동 후 step 증가

# 목표 숫자 k의 좌표 찾기 (0-index 기준)
target_row, target_col = 0, 0
for i in range(n):
    for j in range(n):
        if matrix[i][j] == k:
            target_row, target_col = i, j
            break

# 행렬은 위쪽 행부터 출력 (즉, matrix[0]부터 matrix[n-1]까지)
for row in matrix:
    print(" ".join(map(str, row)))

# k의 위치를 1-index 기준으로 출력
print(target_row + 1, target_col + 1)