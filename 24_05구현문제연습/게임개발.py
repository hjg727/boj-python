N, M = map(int, input().split())

a, b, d = map(int, input().split())
field = []
for i in range(N):
    field.append(list(map(int, input().split())))

def left(direct):
    return (direct+3) % 4

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visited = [[False] * M for _ in range(N)]
field[a][b] = 1
count = 0
result = 1
while True:
    #1단계 :현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 갈 곳 정하기
    d = left(d)
    nx = a + dx[d]
    ny = b + dy[d]

    #아직 가보지않은 칸이 존재한다면, 왼쪽 방향으로 회전한 다음, 한칸을 전진.
    #아니면 다시 왼쪽 방향으로 회전만 수행이후, 1단계
    if not visited[nx][ny] and field[nx][ny] == 0:
        visited[nx][ny] = True
        a = nx
        b = ny
        result += 1
        count = 0
        continue
    else:
        count += 1
    
    #만약 네 방향 모두 이미 가본 칸이거나 바다로 되어있는 칸인 경우, 바라보는 방향 유지, 1칸뒤로 1단계로돌아감.
    #단, 이때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우, break
    if count == 4:
        nx = a - dx[d]
        ny = b - dy[d]

        if field[nx][ny] == 0:
            a = nx
            b = ny
        else:
            break
        count = 0
print(result)
