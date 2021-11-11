n = int(input())
count = 0
queen = [0] * n


# 퀸을 둘 때, 이전 행들에서 뒀던 퀸이 대각선 및 같은 열에 있는지 확인
# 퀸이 있으면 False, 없으면 True
def check(row):
    for i in range(row):
        if queen[row] == queen[i] or abs(queen[row] - queen[i]) == row - i:
            return False
    return True


def dfs(row):
    global count

    if n == row:
        count += 1
        return

    else:
        for i in range(n):
            queen[row] = i

            if check(row):
                dfs(row + 1)
    return


dfs(0)
print(count)
