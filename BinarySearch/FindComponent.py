n = int(input())
arrayN = list(map(int, input().split()))

m = int(input())
arrayM = list(map(int, input().split()))

isStored = False

for i in range(m):
    for j in range(n):
        if arrayM[i] == arrayN[j]:
            isStored = True
    if isStored:
        print('yes', end=' ')
    else:
        print('no', end=' ')
