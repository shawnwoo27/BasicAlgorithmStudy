n = int(input())
coins = list(map(int, input().split()))

coins.sort()

target = 2
store = 0

if coins[0] != '1':
    target = 1

for i in range(len(coins)):
    if coins[i] == target:
        break
    store += len[i]
    if store == target:
        break
    target += 1

print(target)
