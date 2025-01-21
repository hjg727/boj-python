T = int(input())  # 테스트 케이스 수 입력

for test_case in range(1, T + 1):
    N = int(input())  # 농장의 크기
    farm = [list(map(int, input().strip())) for _ in range(N)]  # 농작물 가치

    center = N // 2  # 농장의 중심 좌표
    total_profit = 0  # 수익 초기화

    for row in range(N):
        if row <= center:

            start = center - row
            end = center + row
        else:
            
            start = center - (N - row - 1)
            end = center + (N - row - 1)

        # 범위 내 열 값 합산
        total_profit += sum(farm[row][start:end + 1])#이게 진짜 키포인트 for문보다 간결

    print(f"#{test_case} {total_profit}")