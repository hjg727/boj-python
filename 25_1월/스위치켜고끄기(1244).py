#남자 자기 배수의 수를 바꾸기
#여자 자기포함 자기위치해서 양옆이같으면 바꾸기 안같거나, 인덱스 밖인 경우는 끝내기

def man(switch, n):
    for i in range(n, len(switch), n+1):
        switch[i] = 1 - switch[i]
    return switch

def woman(switch, n):
    switch[n] = 1 - switch[n]
    cnt = 1
    while 0<=(n-cnt) and (n+cnt)<=N-1 and switch[n-cnt] == switch[n+cnt]:
        switch[n-cnt] = 1 - switch[n-cnt]
        switch[n+cnt] = 1 - switch[n+cnt]
        cnt += 1
    return switch

N = int(input())

switch = list(map(int, input().split()))

A = int(input())

for _ in range(A):
    a, b = map(int, input().split())
    if a == 1:
        man(switch, b-1)
    elif a == 2:
        woman(switch, b-1)
for i in range(0, len(switch), 20):
    print(" ".join(map(str, switch[i:i+20])))