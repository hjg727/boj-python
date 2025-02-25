"""
import sys
input = sys.stdin.readline

T = list(input().rstrip())
P = list(input().rstrip())
len_p = len(P)
len_t = len(T)

location = []
for i in range(len_t - len_p + 1):
    if T[i:i+len_p] == P:
        location.append(i+1)

print(len(location))

print(" ".join(map(str, location)))
"""

"""import sys

input = sys.stdin.readline

T = list(input().rstrip())
P = list(input().rstrip())

len_t = len(T)
len_p = len(P)

pattern = [0] * (len_p+1)

tmp = 1
cnt = 0

while tmp != len_p:
    if P[tmp] == P[cnt]:
        tmp += 1
        cnt += 1
        pattern[tmp] = cnt
    else:
        tmp += 1
        cnt = 0

pattern.pop(0)

ans = []

tmp = cnt = 0
#ABCDABD
#pattern 0,0,1,2,0

while tmp != len_t:

    if T[tmp] == P[cnt]:
        tmp += 1
        cnt += 1
    
        if cnt == len_p:#찾았다.
            ans.append(tmp-len_p+1)
            cnt = pattern[cnt-1]
    
    else:
        if cnt != 0:#끊기면 패턴에서 꺼내오기
            cnt = pattern[cnt-1]
        else:
            tmp += 1

print(len(ans))

print(" ".join(map(str, ans)))"""

import sys

input = sys.stdin.readline

T = list(input().rstrip())
P = list(input().rstrip())

len_t = len(T)
len_p = len(P)


pattern = [0] * len_p
j = 0  # 접두사와 접미사가 일치하는 길이 저장

for i in range(1, len_p):
    while j > 0 and P[i] != P[j]:
        j = pattern[j - 1]
    if P[i] == P[j]:
        j += 1
        pattern[i] = j

ans = []
j = 0  # 패턴 내 위치

# KMP 검색 과정
for i in range(len_t):
    while j > 0 and T[i] != P[j]:
        j = pattern[j - 1]
    if T[i] == P[j]:
        if j == len_p - 1:  # 패턴을 찾은 경우
            ans.append(i - len_p + 2)  # 1-based index로 저장
            j = pattern[j]  # 다음 검색을 위해 j 이동\
        else:
            j += 1

print(len(ans))
print(" ".join(map(str, ans)))