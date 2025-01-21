#0, 1, -1? 이기준으로잡아보기
import sys
input = sys.stdin.readline

N = int(input())

positive = []
negative = []
hap = 0

for _ in range(N):
    num = int(input())
    if num > 1:#1은 뭘 곱해도 무의미
        positive.append(num)
    elif num <= 0: #0은,, 음수 지워버리기..?
        negative.append(num)
    else:
        hap += num

positive.sort(reverse=True)
negative.sort()# 제일 큰 수를 갖고있는 음수를 두번째로 큰 수를 갖고있는 음수랑 곱하기


while len(positive) > 1:
    hap += positive.pop(0) * positive.pop(0)# 0 0 안돼면 0 1넣어보기 맞을듯

if positive:
    hap += positive.pop(0)

while len(negative) > 1:
    hap += negative.pop(0) * negative.pop(0)

if negative:
    hap += negative.pop(0)

print(hap)