N = input()

left = 0
right = 0

count = 1
for num in N:
    if count > (len(N) // 2):
        right += int(num)
    else:
        left += int(num)
    count += 1

if right == left:
    print('LUCKY')
else:
    print('READY')