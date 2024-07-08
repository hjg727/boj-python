N = int(input())
M = int(input())
broken = input().split() if M > 0 else []


min_cnt = abs(N-100)


def can_press(channel, broken):
    for num in str(channel):
        if num in broken:
            return False
    return True

min_press = abs(N - 100)

# 0부터 1000000까지 모든 채널을 시도해보기 (1000000은 N의 최대값이 500000이므로, 그 이상으로 설정)
for channel in range(1000000):
    if can_press(channel, broken):
        press = len(str(channel)) + abs(N - channel)
        min_press = min(min_press, press)

print(min_press)