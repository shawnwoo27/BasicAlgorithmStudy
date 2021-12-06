n = int(input())  # 도시의 수 입력

d = list(map(int, input().split()))  # 도시간 거리
oilCost = list(map(int, input().split()))  # 기름 가격

min_oilCost = 10000  # 지금까지의 최소 기름값을 저장할 공간
sum = 0  # 총 기름 리터 수

for i in range(len(d)):
    if oilCost[i] < min_oilCost:
        # 들린 주요소에 기름값이 더 싸면 최솟값 초기화
        min_oilCost = oilCost[i]

    sum += min_oilCost * d[i]

print(sum)

