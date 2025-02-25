#한개의 회의실을 사용하고자하는 N개의회의가있다. 각 회의 I에 대해 시작시간과 끝나느시간이 주어지고
#각 회의가 겹치지 않게 회의실을 사용할 수 있는 최대 개수구하기
#회의시간이 일찍끝나는 순으로 만약 회의시간이 끝나는 시간이 같다면 시작시간이 더 빠른것 순으로
"""sudo
N 입력
회의실 리스트
N 번동안 
시작,끝 시간 입력받기
(시작,끝) 묶어서 리스트에 넣기

정렬 기준: 끝나는시간이 작은 것부터, 같다면, 시작 시간이 작은것부터..?

"""
N = int(input())
meeting = []
for _ in range(N):
    start, end = map(int, input().split())
    meeting.append((start, end))

meeting.sort(key=lambda x : (x[1], x[0]))

count=0
end_time = 0
for i in range(len(meeting)):
    if meeting[i][0] >= end_time:
        end_time = meeting[i][1]
        count+=1

print(count)

