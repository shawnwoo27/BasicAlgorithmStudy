n = int(input())
arr = list(map(int, input().split()))
operators = list(map(int, input().split()))

minimum = 1e+22
maximum = -1e+22


def insert_operator(i, result):
if operators[0] > 0:
    result = arr[i] + arr[i+1]
    operators[0] -= 1
    insert_operator(i+1, result)
    operators[0] += 1

if operators[1] > 0:
    arr[0] - arr[1]
    operators[1] -= 1

if operators[2] > 0:
    arr[0] * arr[1]
    operators[2] -= 1

if operators[3] > 0:
    arr[0] // arr[1]
    operators[3] -= 1




