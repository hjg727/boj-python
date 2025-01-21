N = int(input())
num = 0
num += N // 1000
num += (N % 1000) // 100
num += (N % 100) // 10
num += (N % 10)
print(num)