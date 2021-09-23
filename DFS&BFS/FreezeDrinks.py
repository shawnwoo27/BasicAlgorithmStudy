n, m = map(int, input().split())

frame = []
for i in range(n):
    frame.append(list(map(int, input())))

result = 0

#  print(frame)


def find_0(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if frame[x][y] == 0:
        frame[x][y] = 1
        find_0(x, y + 1)
        find_0(x, y - 1)
        find_0(x + 1, y)
        find_0(x - 1, y)
        return True
    return False


for i in range(n):
    for j in range(m):
        if find_0(i, j):
            result += 1

print(result)
