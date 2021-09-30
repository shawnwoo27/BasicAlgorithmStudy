"""
from collections import deque

n, m = map(int, input().split())

maze = []
for i in range(n):
    maze.append(list(map(int, input())))

distance = []
temp = []
count = 0
d = n+m-1
for i in range(n):
    for j in range(m):
        temp.append((n-i)+(m-j)-1)
        count += 1
        if count % m == 0:
            distance.append(temp)
            temp = []

# print(distance)
# print(maze)

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def bfs(x, y, d):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        if d > distance
        # 4방향
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if maze[nx][ny] == 0:
                continue
            if maze[nx][ny] == 1:
                queue.append((nx, ny))
                d = distance[nx, ny]

    return maze[n - 1][m - 1]


print(bfs(0, 0, d))
"""

# 해당 경우, 해결 불가능
"""
    101111
    101001
    101001
    111001
    111101
"""
