def spiral_pattern_dfs(N):
    # N x N 배열 초기화 (0으로 시작)
    arr = [[0 for _ in range(N)] for _ in range(N)]

    # 이동 방향 (오른쪽, 아래, 왼쪽, 위 순서)
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # 방문한 칸 수 (종료 조건 체크용)
    visited_count = 0
    total_cells = N * N

    def dfs(row, col, direction):
        nonlocal visited_count

        # 현재 위치에 별 찍기
        arr[row][col] = 1
        visited_count += 1

        # 종료 조건: 모든 칸을 방문했으면 종료
        if visited_count == total_cells:
            return

        # 4방향 탐색
        for _ in range(4):
            # 다음 위치 계산
            next_row = row + dirs[direction][0]
            next_col = col + dirs[direction][1]

            # 경계 조건 및 방문 여부 확인
            if (
                0 <= next_row < N and
                0 <= next_col < N and
                arr[next_row][next_col] == 0
            ):
                # 다음 위치로 이동
                dfs(next_row, next_col, direction)
                return  # 현재 방향으로 계속 탐색

            # 방향 전환
            direction = (direction + 1) % 4

    # DFS 시작
    dfs(0, 0, 0)

    return arr


def print_pattern(arr):
    # 배열 출력
    for row in arr:
        print("".join(map(str, row)))


if __name__ == "__main__":
    # 테스트 예제
    N = int(input("Enter an odd number (5 <= N <= 100): ").strip())
    if N < 5 or N > 100 or N % 2 == 0:
        print("N must be an odd number between 5 and 100.")
    else:
        # 나선형 패턴 생성
        pattern = spiral_pattern_dfs(N)
        print_pattern(pattern)