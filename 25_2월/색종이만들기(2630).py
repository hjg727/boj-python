"""# 파랑색 1 하얀색 0
from itertools import chain

N = int(input())
W, B = 0, 0

field = [list(map(int, input().split())) for _ in range(N)]

def all_zero_one(field):
    return len(set(chain(*field))) == 1

def paper_split(field):

    global W, B
    size = len(field)

    if all_zero_one(field):
        if field[0][0] == 1:  # 전체가 1이면 파란색 증가
            B += 1
        else:  # 전체가 0이면 하얀색 증가
            W += 1
        return
    
    mid = size // 2
    field1 = [row[:mid] for row in field[:mid]]
    field2 = [row[mid:] for row in field[:mid]]
    field3 = [row[:mid] for row in field[mid:]]
    field4 = [row[mid:] for row in field[mid:]]

    paper_split(field1)
    paper_split(field2)
    paper_split(field3)
    paper_split(field4)


paper_split(field)

print(W)
print(B)"""

N = int(input())
field = [list(map(int, input().split())) for _ in range(N)]

W, B = 0, 0

def paper_split(x, y, size):
    global W, B
    color = field[x][y]  # 현재 영역의 첫 번째 값

    for i in range(x, x + size):
        for j in range(y, y + size):
            if field[i][j] != color:

                new_size = size // 2
                paper_split(x, y, new_size)
                paper_split(x, y + new_size, new_size)
                paper_split(x + new_size, y, new_size)
                paper_split(x + new_size, y + new_size, new_size)
                return  # 분할했으므로 종료

    # 현재 영역이 모두 같은 색이면 해당 색 개수 증가
    if color == 0:
        W += 1
    else:
        B += 1

# 색종이 나누기 시작 (초기 호출)
paper_split(0, 0, N)

# 결과 출력
print(W)  # 하얀색(0) 개수
print(B)  # 파란색(1) 개수