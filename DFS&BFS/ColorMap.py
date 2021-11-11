def adjacent(i, j):
    if j in tree[i]:
        return True
    return False


def valid(i, c):
    for j in range(1, i):
        if adjacent(i, j) and color[j] == c:
            return False
    return True


def k_coloring(i, c):
    global n
    if valid(i, c):
        color[i] = c

        if i == n:
            return True
        else:
            result = False
            d = 1
            while result == False and d <= k:
                result = k_coloring(i + 1, d)
                d += 1

        return result

    else:
        return False


k = 3  # 이 정도 색으로 충분한지
n = 6
color = [0] * (n + 1)
tree = [
    [],
    [2, 3, 4, 6],
    [1, 5, 6],
    [1, 6],
    [1, 5, 6],
    [2, 4, 6],
    [1, 2, 3, 4, 5]
]

print(k_coloring(1, 1))
