N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

hap = 0
for i in range(N):
    hap += A[i] * B[i]
print(hap)