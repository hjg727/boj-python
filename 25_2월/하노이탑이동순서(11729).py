"""
1. 한 번에 한 개의 원판 만을 "다른 탑으로" 옮길 수 있다.
2. 쌓아 놓은 원판은 항상 위의 원판이 아래의 원판보다 작아야한다.

이동 횟수는 최소

입력은 초기 첫 장대에 쌓인 원판의 개수

출력은 옮긴 횟수 K 출력
수행과정출력 A번째 탑의 가장위에있는원판을 B번째탑의가장위로 옮긴다.
K
A B
A0 B0
A1 B1
An Bn
"""
import sys

sys.setrecursionlimit(10**6)


N = int(input())
ans = []
def move(no, x, y):
    if no > 1:
        move(no-1, x, 6-x-y)
    ans.append((x,y))

    if no > 1:
        move(no-1, 6-x-y, y)

move(N, 1, 3)
print(len(ans))
for x, y in ans:
    print(x, y)