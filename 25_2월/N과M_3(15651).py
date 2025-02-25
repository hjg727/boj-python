"""
1~N까지 자연수 중에서 M개를 고른 수열
중복 허용
"""

N, M = map(int, input().split())
ans = []

def perm(cnt):
    if cnt == M:
        print(" ".join(map(str, ans)))
        return
    
    for i in range(1, N+1):
        ans.append(i)
        perm(cnt+1)
        ans.pop()

perm(0)