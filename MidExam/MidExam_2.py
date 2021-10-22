n = int(input())

arr = []
left = 0
right = 0
set_a = set()

for i in range(n):
    a, b, c = map(int, input().split())
    set_a.append(a)
    arr.append([b, c])

for i in range(n-1):
    check_overlap(arr[i][0], arr[i][1], arr[i+1][0], arr[i+1][1])


def check_overlap(b1, c1, b2, c2):
    global left, right

    left = 0
    right = 0

    if b1 <= b2 <= c1:
        left = b2
        right = c1

        if b1 <= c2 <= c1:
            left = b2
            right = c2

    if b2 <= b1 <= c2:
        left = b1
        right = c2

        if b2 <= c1 <= c2:
            left = b1
            right = c1

    if left == 0:
        return False
    else:
        return True

print(arr)