N = int(input())
words = set()
for _ in range(N):
    words.add(str(input().rstrip()))
words = list(words)
words.sort(key=lambda x: (len(x), x))

for word in words:
    print(word)