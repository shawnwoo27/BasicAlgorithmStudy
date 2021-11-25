import sys

n, m = map(int, input().split())

graph = [None] * n

for i in range(n):
    graph[i] = []

max_cost = 0
for i in range(m):
    x, y, z = map(int, input().split())
    graph[y].append((x, z))
    graph[x].append((y, z))
    max_cost += z
    print(graph)

start = 0
visited = [False] * n
D = [sys.maxsize] * n
D[start] = 0
previous = [None] * 7
previous[start] = 0

for i in range(n):
    m = -1
    min_value = sys.maxsize
    for j in range(n):
        if not visited[j] and D[j] < min_value:
            min_value = D[j]
            m = j
    visited[m] = True

    for vNum, distance in list(graph[m]):
        if not visited[vNum]:
            if distance < D[vNum]:
                D[vNum] = distance
                previous[vNum] = m

min_cost = 0
for i in range(1, n):
    min_cost += D[i]

print('maximum cost: ', max_cost)
print('minimum cost: ', min_cost)
print('최대 절약 금액: ', max_cost - min_cost)
