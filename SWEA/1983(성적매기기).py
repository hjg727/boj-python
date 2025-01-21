T = int(input())

def calculate(score):
    return score[0]*0.35 + score[1]*0.45 + score[2]*0.2

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    student = [list(map(int, input().split())) for _ in range(N)]
    cnt = N//10

    for i in range(N):
        student[i] = [calculate(student[i])]
    
    target = student[K-1]
    sort_score = sorted(student, reverse=True)
    
    rating = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]
    tmp = 0
    for i in range(0, N, cnt):
        for j in range(cnt):
            sort_score[i+j] = [sort_score[i + j], rating[tmp]]
        
        tmp += 1
    
    for score in sort_score:
        if target == score[0]:
            print(f"#{test_case} {score[1]}")
            break