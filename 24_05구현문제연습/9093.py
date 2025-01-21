#단어 뒤집기
T = int(input())

str_list = [[] for _ in range(T)]

for i in range(T):
    a = list(map(str, input().split()))
    for j in range(len(a)):
        a[j] = ''.join(reversed(a[j]))  # reversed가 반환하는 것을 문자열로 변환
    str_list[i] = a

for i in range(T):
    print(" ".join(str_list[i]))  # 최종 결과 출력

"""
import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    st = input().split()
    print(" ".join(st[::-1])[::-1])
"""