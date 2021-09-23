n = int(input())
coins = list(map(int, input().split()))

coins.sort()
minimum = 1

for i in coins:
    if i > minimum:
        break
    minimum += i

print(minimum)
