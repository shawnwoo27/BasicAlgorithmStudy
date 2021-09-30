n = int(input())
m = int(input())

network = []
result = 0

for i in range(m):
    x, y = map(int, input().split())
    network.append([x, y])

#  print(network)


def dfs(graph, num, visited):
    global result
    visited[num] = True
    for i in graph[num]:
        if visited[i]:
            dfs(graph, i, visited)
            result += 1


visited = [False] * m

dfs(network, 1, visited)
print(result)
