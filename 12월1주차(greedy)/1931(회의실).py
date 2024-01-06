import sys
input = sys.stdin.readline


N = int(input())

meeting = []
count = 0

for _ in range(N):
    start, end = map(int, input().split())
    meeting.append((start, end))

meeting.sort(key=lambda x: (x[1], x[0]))

#선택된 회의의 끝나는 시간 저장
end_time = 0
for i in range(len(meeting)):
    if meeting[i][0] >= end_time:
        end_time = meeting[i][1]
        count += 1
print(count)