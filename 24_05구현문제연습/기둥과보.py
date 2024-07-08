def solution(n, build_frame):
    # 필드 초기화
    field_x = [[0] * (n + 1) for _ in range(n + 1)]
    field_y = [[0] * (n + 1) for _ in range(n + 1)]

    # 결과 저장 리스트
    check_build = []

    for x, y, a, b in build_frame:
        # 기둥 설치
        if a == 0:
            if y == 0 or field_x[x][y] == 1 or (field_y[x][y] == 1 or (x > 0 and field_y[x-1][y] == 1)):
                if b == 1:
                    check_build.append([x, y, a])
                    field_x[x][y + 1] = 1
                elif b == 0 and ([x, y, a] in check_build):
                    check_build.remove([x, y, a])
                    field_x[x][y + 1] = 0
        # 보 설치
        else:
            if (y > 0 and (field_x[x][y] == 1 or field_x[x + 1][y] == 1)) or (x > 0 and field_y[x - 1][y] == 1 and field_y[x + 1][y] == 1):
                if b == 1:
                    check_build.append([x, y, a])
                    field_y[x][y] = 1
                    field_y[x + 1][y] = 1
                elif b == 0 and ([x, y, a] in check_build) and (x < n and field_y[x + 1][y] == 1 or x > 0 and field_y[x - 1][y] == 1):
                    check_build.remove([x, y, a])
                    field_y[x][y] = 0
                    field_y[x + 1][y] = 0

    # 정렬 및 반환
    check_build.sort()
    return check_build

#위 코드는 예시 입력 결과만 정답으로 나온다. 문제점을 찾아보자.
"""
위 코드가 오답인 이유가 대부분이 런타임에러이다.

"""