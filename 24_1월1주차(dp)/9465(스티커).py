import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    N = int(input())
    stick = [list(map(int, input().split())) for _ in range(2)]

    if N > 1:
        stick[0][1] = stick[0][1] + stick[1][0]
        stick[1][1] = stick[1][1] + stick[0][0]

        for i in range(2, N):
            stick[0][i] += max(stick[1][i-1], stick[1][i-2])
            stick[1][i] += max(stick[0][i-1], stick[0][i-2])
    print(max(stick[0][N-1], stick[1][N-1]))#N-1인이유 range.
