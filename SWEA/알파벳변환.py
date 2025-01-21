alpha = str(input())

def alphaconvert(alphabet):
    return ord(alphabet.upper()) - ord('A') + 1
res = []
for i in range(len(alpha)):
    res.append(alphaconvert(alpha[i]))

print(" ".join(map(str, res)))
