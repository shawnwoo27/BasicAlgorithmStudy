n, m = map(int, input().split())
weight = list(map(int, input().split()))

array = [0] * 10
result = 0

for i in weight:
    array[i-1] += 1

for i in range(m):
    n -= array[i]
    result += array[i] * n

print(result)
