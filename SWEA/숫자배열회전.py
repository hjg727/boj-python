def clock_90(num):
    return [list(reversed(col)) for col in zip(*num)]

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    num = []
    for _ in range(N):
        num.append(list(map(int, input().split())))
    num_90 = clock_90(num)
    num_180 = clock_90(num_90)
    num_270 = clock_90(num_180)

    print(f"#{test_case}")
    for (row1, row2, row3) in zip(num_90, num_180, num_270):
        print("".join(map(str, row1)), "".join(map(str, row2)), "".join(map(str, row3)))

def rotate_counterclockwise(matrix):
    # zip과 리스트 컴프리헨션을 사용하여 반시계방향으로 회전
    return [list(col) for col in zip(*matrix[::-1])]

def rotate_clockwise(matrix):
    # 시계방향 90도 회전
    return [list(reversed(col)) for col in zip(*matrix)]

"""
bfs, dfs, Back 에 대해서 익숙해지고싶은데 단계(알고리즘익히는 기초문제, 응용하는 응용 문제)별로 문제를 알려줘
SWEA D3문제 풀면서
외우는거지
오늘 너 시간 어떻게 돼
16:30->헬스
수업-> 코테풀기
최대 30분..?만 고민하기 (타이머 썼어)
오늘 2시자기?
플젝 14시~19시?
토요일 23시59분
일요일 12시20분
"""