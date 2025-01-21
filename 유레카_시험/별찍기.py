def print_triangle(n):
    for i in range(1, n + 1):
        print(' ' * (n - i), end='')
        print('*' * (2 * i - 1))

# 사용 예시
n = 5  # 삼각형 높이
print_triangle(n)