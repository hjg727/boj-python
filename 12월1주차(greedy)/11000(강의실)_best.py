from heapq import heappush, heappop
import sys
input = sys.stdin.readline

n = int(input())
lecture = sorted([tuple(map(int,input().split())) for _ in range(n)], key=lambda x: x[0])

room = []
#강의
heappush(room, lecture[0][1])

for i in range(1, n):
    if room[0] > lecture[i][0]:
        heappush(room, lecture[i][1])
    else:
        heappop(room)#기존의 수업을 삭제
        #기존의 수업 이후의 시작할 수업의 끝날 시간 저장
        heappush(room, lecture[i][1])
print(len(room))