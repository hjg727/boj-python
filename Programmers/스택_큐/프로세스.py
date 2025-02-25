"""
1. 대기중인 큐에서 프로세스 하나 꺼내기
2. 큐안에 우선순위가 더 높은 프로세스가 있다면 1에서 꺼낸 것 다시 큐에 넣기
    3. 없다면 방금 꺼낸 거 실행
    3.1 한번 실행한 프로세스는 다시 큐에 넣지 않고 종료

location 인덱스에 있는 프로세스가 언제 실행하는 지 리턴
"""

from collections import deque
priorities = [1,1,9,1,1,1]


def solution(priorities, location):
    priorities = deque(priorities)
    cnt = 0

    while priorities:
        best = max(priorities)

        front = priorities.popleft()
        location -= 1

        if front == best:
            cnt += 1
            if location < 0:
                return cnt
        else:
            priorities.append(front)
            if location < 0:
                location = len(priorities) - 1

print(solution(priorities, 0))
            