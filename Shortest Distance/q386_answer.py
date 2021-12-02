INFINITE = int(1e9)  # 임의에 무한대값

n, m = map(int, input().split())  # 학생 수(노드 수), 간선 수 입력

# 노드 수^2 크기의 그래프 생성
graph = [[INFINITE] * (n + 1) for _ in range(n + 1)]

# 같은 학생의 경우 거리 비용을 0으로
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# a < b 입력 시, 두 학생의 거리를 1로 둠
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

# 각 학생을 거쳐가며, 그래프 갱신
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = 0

# i학생 기준으로, 몇명의 학생과 연결되있는지 세기
for i in range(1, n + 1):
    # 기준이 되는 학생이 바뀔 때마다, 연결된 학생 수 초기화
    count = 0

    # i학생과 j학생은 이어져있으므로, 뒤집어서도 체크
    for j in range(1, n + 1):
        if graph[i][j] != INFINITE or graph[j][i] != INFINITE:
            count += 1
            
    # 연결된 학생 수가 총학생 수와 같다면, 순위를 알 수 있는 학생 1 추가
    if count == n:
        result += 1

print(result)
