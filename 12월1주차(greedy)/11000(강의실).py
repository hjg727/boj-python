import sys

input = sys.stdin.readline

n = int(input())
time_table = []*n

for _ in range(n):
    a, b = map(int, input().split())
    time_table.append((a, b))


time_table.sort()

end_time = time_table[0][1]
room = 1
for i in range(1, n):
    if time_table[i][0] >= end_time:
        end_time = time_table[i][1]
    else:
        room += 1#뭔가이상한데..
print(room)