n = int(input())

array = []
for i in range(n):
    inputValue = input().split()
    array.append([inputValue[0], int(inputValue[1])])

array.sort(key=lambda x: x[1])

for i in array:
    print(i[0], end=' ')
