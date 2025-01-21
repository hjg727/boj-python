a, b = map(int, input().split())

if a-1 == b or a+2 == b:
    print("A")
elif a+1 == b or a-2 == b:
    print("B")