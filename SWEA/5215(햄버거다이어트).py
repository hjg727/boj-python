T = int(input())

for test_case in range(1, T+1):

    N, limit = map(int, input().split())
    ingredient = []
    

    for _ in range(N):
        a, b = map(int, input().split())
        ingredient.append((a, b))
    
    max_score = 0

    def calculate(index, current_score, current_calorie, limit):

        global max_score

        if current_calorie > limit:
            return
        
        max_score = max(max_score, current_score)

        for i in range(index, N):
            taste, calorie = ingredient[i]
            calculate(i+1, current_score+taste, current_calorie+calorie, limit)
    
    calculate(0,0,0,limit)

    print(f"#{test_case} {max_score}")
