N, K = map(int, input().split())

res = 1

def move(x):
    if x == 0:
        return -1
    elif x == 1:
        return +1
    elif x == 2:
        return 2

dist = []


while N != K:
    for i in range(3):
        tmp = 0
        if i == 2:
            tmp = N * move(i)
        else:
            tmp = N + move(i)
        
        dist.append([abs(K-tmp), tmp])

    dist.sort(key = lambda x : x[0])
    N = dist[0][1]
    
    res += 1
    dist.clear()

print(res)