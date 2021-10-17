n = int(input())
arr = list(map(int, input().split()))
operators = list(map(int, input().split()))

minimum = 1e+22
maximum = -1e+22


def insert_operator(i, result):
    global minimum, maximum

    if i == n:
        minimum = min(minimum, result)
        maximum = max(maximum, result)

    else:
        if operators[0] > 0:
            operators[0] -= 1
            insert_operator(i + 1, result + arr[i])
            operators[0] += 1

        if operators[1] > 0:
            operators[1] -= 1
            insert_operator(i + 1, result - arr[i])
            operators[1] += 1

        if operators[2] > 0:
            operators[2] -= 1
            insert_operator(i + 1, result * arr[i])
            operators[2] += 1

        if operators[3] > 0:
            operators[3] -= 1
            insert_operator(i + 1, result // arr[i])
            operators[3] += 1


insert_operator(1, arr[0])
print(maximum)
print(minimum)
print(-1//3)





