n = int(input())

ugly = [1]


# 1 // n
# 1 + 3 // n
# 1 + 3 + 9 // n
# 1 + 3 + 9 + 27 // n
# 1 + 3 + 9 + 27 + 81 // n
# .
# .
# .
# 해당 식이 1이 되면, n-1번째 반복의 식을 활용
def get_repeat_num():
    temp = 0
    i = 0

    while True:
        temp += 3**i
        target = temp // n

        if target == 1:
            return i

        i += 1


def multiply(num, r):
    global repeat

    if repeat < r:
        return

    add2 = num * 2
    add3 = num * 3
    add5 = num * 5

    ugly.append(add2)
    ugly.append(add3)
    ugly.append(add5)

    multiply(add2, r + 1)
    multiply(add3, r + 1)
    multiply(add5, r + 1)


repeat = get_repeat_num()
print(repeat)
multiply(1, 1)

ugly.sort()

print(ugly)
new_ugly = []
for item in ugly:
    if item not in new_ugly:
        new_ugly.append(item)

print(new_ugly)
print(new_ugly[n-1])
