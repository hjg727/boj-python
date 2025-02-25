"""import itertools

N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]
permutation = itertools.permutations(arr, M)

for per in permutation:
    print(*per)"""

"""N, M = map(int, input().split())
ans = [0] * M
visited = [False] * (N+1)

def perm(cnt):
    if cnt == M:
        print(" ".join(map(str, ans)))
        return
    
    for i in range(1, N+1):
        if visited[i]:
            continue
        visited[i] = True
        ans[cnt] = i
        perm(cnt+1)
        visited[i] = False

perm(0)
"""

N, M = map(int,input().split())

ans = []

def perm(cnt):
    if cnt == M:
        print(" ".join(map(str, ans)))
        return
    
    for i in range(1, N+1):
        if i not in ans:
            ans.append(i)
            perm(cnt+1)
            ans.pop()

perm(0)
