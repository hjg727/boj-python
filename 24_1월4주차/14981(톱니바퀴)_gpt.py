from collections import deque

# 톱니바퀴 상태 입력받기
gear = [deque(list(map(int, input().strip()))) for _ in range(4)]

def rotate(gear, direction):
    if direction == 1:  # 시계 방향
        temp = gear.pop()
        gear.appendleft(temp)
    else:  # 반시계 방향
        temp = gear.popleft()
        gear.append(temp)

# 회전 명령 수 입력받기
K = int(input())

for _ in range(K):
    target, direction = map(int, input().split())
    target -= 1  # 인덱스는 0부터 시작하므로

    # 각 톱니바퀴의 회전 여부와 방향 저장
    rotate_dir = [0]*4
    rotate_dir[target] = direction

    # target 톱니바퀴 왼쪽 확인
    temp_dir = direction
    for i in range(target-1, -1, -1):
        if gear[i][2] != gear[i+1][6]:  # 극이 다른 경우
            temp_dir *= -1  # 회전 방향 반대로
            rotate_dir[i] = temp_dir
        else:  # 극이 같은 경우
            break

    # target 톱니바퀴 오른쪽 확인
    temp_dir = direction
    for i in range(target+1, 4):
        if gear[i][6] != gear[i-1][2]:  # 극이 다른 경우
            temp_dir *= -1  # 회전 방향 반대로
            rotate_dir[i] = temp_dir
        else:  # 극이 같은 경우
            break

    # 각 톱니바퀴 회전
    for i in range(4):
        if rotate_dir[i] != 0:
            rotate(gear[i], rotate_dir[i])

# 점수 계산
score = sum([(gear[i][0] * (2 ** i)) for i in range(4)]) #배워야될 부분
print(score)