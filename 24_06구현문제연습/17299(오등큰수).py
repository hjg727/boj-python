import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))

num_list = Counter(A) #출현횟수 1이 3번 출현하면 1 : 3

index_stack = []
result = [-1] * N

for i in range(N):
    # 스택이 비어있지 않고 현재 원소가 스택 top의 원소의 출현 횟수보다 크면
    while index_stack and num_list[A[index_stack[-1]]] < num_list[A[i]]:
        # 스택에서 인덱스를 꺼내고 '오등큰수'로 현재 원소를 등록
        index = index_stack.pop()
        result[index] = A[i]
    # 현재 인덱스를 스택에 추가
    index_stack.append(i)

for i in range(len(result)):
    print(result[i], end=" ")