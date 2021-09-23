n = int(input())
fear = list(map(int, input().split()))

fear.sort
count = 0

while True:
    brave = fear[0]

    if brave > len(fear):
        break
    elif brave == len(fear):
        count += 1
        break

    del fear[:fear[0]]
    # print(fear)

    count += 1

print(count)

