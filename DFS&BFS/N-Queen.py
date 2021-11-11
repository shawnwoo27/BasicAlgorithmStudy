def promising(queen, row):
    for i in range(row):
        # 이전 row의 직선, 대각선에 있는지 모두 조사한다.
        if (queen[row] == queen[i]) or (row - i == abs(queen[row] - queen[i])):
            return False
    return True


def dfs(queen, row, n):
    global count

    if n == row:
        # 끝까지 도달했으면 count 증가함
        count += 1
        return

    for col in range(n):
        queen[row] = col

        if promising(queen, row):
            # 새로 두고자 하는 곳이 유효한지 조사한다.
            dfs(queen, row + 1, n)
            # 둬도 된다면 다음 행으로 넘어감
    return


n = int(input())
count = 0
queen = [0] * n  # 어차피 같은 행에는 두지 못함. n*n판에서 퀸의 최대 개수는 n을 넘어설 수 없음
dfs(queen, 0, n)
print(count)
