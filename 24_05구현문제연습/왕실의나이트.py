start = input()

if type(start[0]) == str:
    start_x = int(ord(start[0])) - int(ord('a')) + 1
else:
    print(0)
start_y = int(start[1])


# char_to_number = {
#     'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5,
#     'f': 6, 'g': 7, 'h': 8
# }

# start_x = 0
# start_y = 0
# if start[0].isalpha():
#     start_x += char_to_number[start[0]]
# if start[1].isdigit():
#     start_y += int(start[1])

steps = [(-1, 2), (1, 2), (-1, -2), (1, -2), (2, -1), (2, 1), (-2, -1), (-2, 1)]

count = 0

for step in steps:
    nx = start_x + step[0]
    ny = start_y + step[1]

    if 1 <= nx < 9 and 1 <= ny < 9:
        count += 1

print(count)