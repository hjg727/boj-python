N = int(input())


for _ in range(N):
    vps = input()
    balance = 0

    no_state = False
    for char in vps:
        if char =='(':
            balance += 1
        elif char ==')':
            if balance == 0:
                no_state = True
                break
            else:
                balance -= 1

    if balance == 0 and not no_state:
        print("YES")
    else:
        print("NO")