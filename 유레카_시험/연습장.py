"""N = int(input())

words = []

for _ in range(N):
    words.append(input().strip())

def group_word(word):
    seen = set()
    prev = ''

    for char in word:
        if char != prev:
            if char in seen:
                return False
            seen.add(char)
        prev = char

    return True

ans = sum(group_word(word) for word in words)

print(ans)"""

"""N = int(input())

num = str(input().rstrip())
ans = 0
for i in range(N):
    ans += int(num[i])
print(ans)"""

N, M = map(int, input().split())
box = [i for i in range(1, N+1)]
commend = []
for _ in range(M):
    i, j = map(int,input().split())
    commend.append((i-1,j-1))

for i, j in commend:
    box[i:j+1] = box[i:j+1][::-1]

print(" ".join(map(str, box)))