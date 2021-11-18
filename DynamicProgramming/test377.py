n = int(input())
t = []
money = []
d = [0] * n
max_money = 0

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    money.append(y)

for i in range(n-1, -1, -1):
    time = t[i] + 1
    if time <= n:
        d[i] = max(money[i] + d[time], max_money)
        max_money = d[i]
    else:
        d[i] = max_money
