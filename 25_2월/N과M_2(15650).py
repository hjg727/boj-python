N, M = map(int, input().split())

ans = []

def perm(cnt, ans):
    if len(ans) == M:
        print(" ".join(map(str, ans)))
        return
    
    for i in range(cnt, N+1):
        ans.append(i)
        perm(i+1, ans)
        ans.pop()

perm(1, ans)

"""N, M = map(int,input().split())
def BT(start, N, M, path):
    if len(path) == M:
        print(' '.join(map(str, path)))
        return

    for i in range(start, N + 1):
        path.append(i)
        BT(i + 1, N, M, path)
        path.pop()

BT(1, N, M ,[])
"""