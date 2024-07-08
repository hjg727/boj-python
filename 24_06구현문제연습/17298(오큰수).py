import sys
input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))

index_stack = []
result = [-1] * N

for i in range(N):
    # 스택이 비어있지 않고 현재 원소가 스택 top의 원소보다 크면
    while index_stack and A[index_stack[-1]] < A[i]:
        # 스택에서 인덱스를 꺼내고 '오큰수'로 현재 원소를 등록
        index = index_stack.pop()
        result[index] = A[i]
    # 현재 인덱스를 스택에 추가
    index_stack.append(i)

for i in range(len(result)):
    print(result[i], end=" ")




"""
해당 방법은 브루트포스 방식이다.

A = [0] + list(map(int, input().split()))

res = []

for i in range(1, N+1):
    for j in range(i, N+1):
        if A[i] < A[j]:
            res.append(A[j])
            break
        
        if j == N:
            if A[i] < A[j]:
                res.append(A[j])
            else:
                res.append(-1)


for i in range(len(res)):
    print(res[i], end = " ")
"""