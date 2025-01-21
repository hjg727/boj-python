N = int(input())

a = list(map(int, input().split()))
a.sort()
length = len(a) - 1

print(a[length // 2])