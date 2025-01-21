T = int(input())

def compare(x, y):

    if x < y:
        return "<"
    elif x > y:
        return ">"
    elif x == y:
        return "="

for test_case in range(1, T+1):
    x, y = map(int, input().split())
    print(f"#{test_case} ", compare(x, y))