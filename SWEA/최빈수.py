T = int(input())

for _ in range(T):
    test_case = int(input())
    num = [0] * 101
    score = list(map(int, input().split()))

    for i in score:
        num[i] += 1
    
    max_cnt = max(num)

    most_frequent_score = max(i for i, count in enumerate(num) if count == max_cnt)
    
    print(f"#{test_case} {most_frequent_score}")