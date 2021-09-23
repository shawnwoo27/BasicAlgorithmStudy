#  deque는 list와 거의 흡사
#  단, deque에는 appendleft와 popleft같은 메서드들이 추가로 존재
from collections import deque

n, m = map(int, input().split())

maze = []
for i in range(n):
    maze.append(list(map(int, input())))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def bfs(x, y):
    queue = deque()  # 빈 deque 객체 생성
    queue.append((x, y))

    # queue가 비어있지 않다면, 반복 실행
    while queue:
        # 맨 왼쪽 요소 기준으로 뽑아내기, pop과 반대 방향. list에 pop(0)과 같다
        x, y = queue.popleft()

        # 4방향
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if maze[nx][ny] == 0:
                continue
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))

    return maze[n - 1][m - 1]


print(bfs(0, 0))
