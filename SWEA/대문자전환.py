sentence = str(input())

#문자열은 불변이므로, 소문자면 -> 대문자로 변환

sentence = list(sentence[:-1])

for i in range(len(sentence)):
    if sentence[i].islower():
        sentence[i] = sentence[i].upper()

res = "".join(sentence)
print(f"{res}.")