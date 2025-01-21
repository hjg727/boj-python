for test_case in range(1, 11):
    dump = int(input())
    field = list(map(int, input().split()))

    while dump:
        field[field.index(max(field))] -= 1
        field[field.index(min(field))] += 1
        dump -= 1
    res = field[field.index(max(field))] - field[field.index(min(field))]
    print(f"#{test_case} {res}")