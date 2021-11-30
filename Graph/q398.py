import sys

n = int(input())

graph = [None] * n

for i in range(n):
    graph[i] = []

x_list = []
y_list = []
z_list = []

for i in range(n):
    x, y, z = map(int, input().split())
    x_list.append((i, x))
    y_list.append((i, y))
    z_list.append((i, z))

x_list.sort(key=lambda e: e[1])
y_list.sort(key=lambda e: e[1])
z_list.sort(key=lambda e: e[1])

print(x_list)
print(y_list)
print(z_list)


def build_edge(list_name):
    for i in range(len(list_name) - 1):
        graph[list_name[i][0]].append((list_name[i + 1][0], abs(list_name[i][1] - list_name[i + 1][1])))
        graph[list_name[i+1][0]].append((list_name[i][0], abs(list_name[i][1] - list_name[i + 1][1])))


build_edge(x_list)
build_edge(y_list)
build_edge(z_list)

start = 0
visited = [False] * n
D = [sys.maxsize] * n
D[start] = 0

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

min_cost = 0
for i in range(1, n):
    min_cost += D[i]

print(graph)
print('최소 비용: ', min_cost)
