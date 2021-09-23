n, m = map(int, input().split())

d = [[0] * m for _ in range(n)]  # n * m 맵, 가보지 않은 곳 0

x, y, direction = map(int, input().split())  # 현재좌표, 보고있는 방향 입력
d[x][y] = 1  # 현재 좌표 방문 처리

# 맵 지형 입력
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 방향값 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# 좌회전(반시계 90도)
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


count = 1
turn_time = 0  # 회전 횟수
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 가보지 않은 칸이 존재
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue

    # 가보지 않은 칸 X, 또는 바다
    else:
        turn_time += 1

    # 네 방향 모두 X
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        # 뒤로 이동
        if array[nx][ny] == 0:
            x = nx
            y = ny

        # 뒤가 바다로 막힘
        else:
            break
        turn_time = 0

print(count)
