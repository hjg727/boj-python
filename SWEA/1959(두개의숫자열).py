T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())

    if N <= M:
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
    else:
        B = list(map(int, input().split()))
        A = list(map(int, input().split()))

    res = float('-inf')

    for start in range(len(B) - len(A) + 1):
        tmp = 0

        for i in range(len(A)):
            tmp += A[i] * B[start+i]
        
        if res < tmp:
            res = tmp

    print(f"#{test_case} {res}")