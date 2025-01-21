T = int(input())

for test_case in range(1, T+1):
    word = str(input())

    r_word = word[::-1]
    res = 1 if r_word == word else 0
    print(f"#{test_case} {res}")