#  미완성
n = int(input())  # 음식 개수
food_times = list(map(int, input().split()))  # 각 음식당 먹는데 걸리는 시간
k = int(input())  # 방송 중단 시간

dic = {}

for i in range(len(food_times)):
    dic[food_times[i]] = i+1

food_times.sort()

if sum(food_times) <= k:
    result = -1
else:
    for i in range(len(food_times)):
        if k > food_times[i] * n:
            k -= food_times[i] * n
            n -= 1
            del dic[food_times[i]]
        else:
            break

print(result)
