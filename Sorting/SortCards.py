n = int(input())
array = []
for i in range(n):
    array.append(int(input()))

result = 0

for i in range(n-1):
    array.sort()
    result += array[0] + array[1]
    array[0] = array[0] + array[1]
    array[1] = 10001
    print(array)

print(result)
