import sys
input = sys.stdin.readline


N, M, R = map(int, input().split())

field = [list(map(int, input().split())) for _ in range(N)]

command= list(map(int,input().split()))

def updown(field):# 1번 연산
    return field[::-1]

def side(field):# 2번 연산
    return [row[::-1] for row in field]

def right_90(field):# 3번 연산
    return [list(reversed(col)) for col in zip(*field)]

def left_90(field):# 4번 연산
    return [list(col) for col in zip(*field)][::-1]



def right_push(field): # 5번 연산
    n = len(field)
    m = len(field[0])
    height = n//2
    width = m//2
    
    #4등분을 하고 아예 새곳에다가 배정해버리자
    """
    A 좌상단
    B 우상단
    C 좌하단
    D 우하단
    """
    A = [row[:width] for row in field[:height]]
    B = [row[width:] for row in field[:height]]
    C = [row[:width] for row in field[height:]]
    D = [row[width:] for row in field[height:]]

    ans = [[0]*m for _ in range(n)]

    #A -> B , B -> D, D -> C, C -> A
    for i in range(height):
        ans[i][width:] = A[i]
        ans[i+height][width:] = B[i]
        ans[i+height][:width] = D[i]
        ans[i][:width] = C[i]

    return ans       

def left_push(field):
    n = len(field)
    m = len(field[0])
    height = n//2
    width = m//2
    
    A = [row[:width] for row in field[:height]]
    B = [row[width:] for row in field[:height]]
    C = [row[:width] for row in field[height:]]
    D = [row[width:] for row in field[height:]]

    ans = [[0]*m for _ in range(n)]
    #A -> C, C->D, D->B, B->A
    for i in range(height):
        ans[i][:width] = B[i]
        ans[i+height][:width] = A[i]
        ans[i+height][width:] = C[i]
        ans[i][width:] = D[i]
    return ans

for i in command:
    if i == 1:
        field = updown(field)
    elif i == 2:
        field = side(field)
    elif i == 3:
        field = right_90(field)
    elif i == 4:
        field = left_90(field)
    elif i == 5:
        field = right_push(field)
    elif i == 6:
        field = left_push(field)

for row in field:
    print(" ".join(map(str, row)))