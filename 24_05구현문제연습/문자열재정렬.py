all = input()

alpha = ''.join(sorted(filter(str.isalpha, all)))
digit = sum(int(i) for i in all if i.isdigit())

print(alpha+str(digit))

"""
all = input()

int_hap = 0
alpha = []


for i in all:
    if i.isdigit():
        int_hap += int(i)
    elif i.isalpha():
        alpha.append(i)

alpha=sorted(alpha)
print(alpha+str(int_hap))
"""