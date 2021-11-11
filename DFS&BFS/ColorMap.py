# i번 노드가 j번 노드와 인접한지 확인
def adjacent(i, j):
    if j in graph[i]:
        return True
    return False


# 인접한 노드들과 색이 겹치지 않는지 확인
def valid(i, c):
    for j in range(1, i):
        if adjacent(i, j) and color[j] == c:
            return False
    return True


def k_coloring(i, c):
    global n
    if valid(i, c):
        color[i] = c

        if i == n:
            return True
        else:
            result = False
            d = 1  # 임시 색깔. 재귀를 돌며 항상 1번부터 k번 색까지 칠할 수 있도록
            while result is False and d <= k:
                result = k_coloring(i + 1, d)
                d += 1

        return result

    else:
        return False


k = 3  # 이 정도 색으로 충분한지
n = 6  # 노드의 수, 색칠할 칸의 수
color = [0] * (n + 1)
graph = [
    [],
    [2, 3, 4, 6],
    [1, 5, 6],
    [1, 6],
    [1, 5, 6],
    [2, 4, 6],
    [1, 2, 3, 4, 5]
]

print(k_coloring(1, 1))  # 1번 노드, 1번 색깔부터 확인
