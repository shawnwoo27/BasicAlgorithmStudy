n = int(input())
array = []
for i in range(n):
    array.append(int(input()))

array.sort()
s = 0
s += (array[0] + array[1]) * (n-1)

for i in range(2, n):
    s += array[i] * (n-i)

print(s)
