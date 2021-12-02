INFINITE = int(1e9)  # 임의에 무한대값

n = int(input())  # 도시 수 입력
m = int(input())  # 간선 수 입력

# 도시 * 도시 만큼 그래프 생성 (0값 무시)
graph = [[INFINITE] * (n + 1) for _ in range(n + 1)]

# 같은 도시의 경우 거리 비용을 0으로
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 도시끼리의 거리 입력 및 저장
for _ in range(m):
    a, b, c = map(int, input().split())

    # 기존 경로보다 짧은 경로만 저장
    if c < graph[a][b]:
        graph[a][b] = c

# 각 노드를 거쳐 가며, 그래프를 갱신
for k in range(1, n + 1):
    for a in range(1, n + 1):
        if a == k:
            continue
        for b in range(1, n + 1):
            if a == b:
                continue
            if b == k:
                continue
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 그래프 내에 값들을 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        # 갈 수 없는 경우를 0 으로 출력
        if graph[a][b] == INFINITE:
            print(0, end=" ")
        else:
            print(graph[a][b], end=" ")
    print()
