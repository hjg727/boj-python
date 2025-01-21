"""
채널 0~inf
보고있는 채널 100
이동 하려는 곳은 N
어떤 버튼이 고장났을때
채널N까지갈때 최소 몇번을 눌러야하
정리
1. 리모콘에서 고장난 버튼의 정보가 주어진다.
2. 해당 리모콘으로 N번의 채널로 갈때까지 숫자 및 +,-를 누를때마다 cnt 1개씩올라간다.
3. 최소 cnt갯수 출력

마지막 생각 정리
1. 일단 주어진 숫자버튼으로 N에 최대한 가깝게간다.(동시에 버튼을 누른횟수 cnt에 더하기)
   -맨앞자리부터 갖고있는리모콘버튼에서 제일가까운 값을 넣기
   -맨끝자리까지 이를 반복
2. 나머지는 +할지, -할지 해당 버튼에 대한 뺀값의 절댓값이 더 작은 쪽을 선택하고
3. 그 뺀값을 cnt에 더한다.
"""

remote = [i for i in range(10)]
N = int(input())
M = int(input())

nums = input()
num = [int(num) for num in nums.split()]
for i in range(M):
    remote.remove(num[i])

if N == 100:
    print(0)
    exit(0)

#일단 현재채널에서 +,-로 N에 접근한 버튼횟수를 res에 저장
res = abs(N-100)

sub_value = ""
cnt = 0

for char in str(N):#[5457]
    min_diff = 1e9
    close_num = 0
    for i in remote:#[1,2,3,4,5,9]
        value = abs(int(char) - i)

        if value < min_diff:# 해당 값을 저장하기위해
            min_diff = value
            close_num = i
        elif value == min_diff:
            close_num = min(close_num, i)

    sub_value += str(close_num)
    cnt+=1

cnt = (cnt + abs(N - int(sub_value)))

print(min(res, cnt))