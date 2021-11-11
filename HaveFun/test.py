def dfs(l):
    global cnt
    if l == select:
        for i in range(select):
            print(res[i], end=' ')
        print()
        cnt += 1
    else:
        for i in range(1, len(arr) + 1):
            res[l] = i
            dfs(l + 1)


arr = [1, 2, 3, 4, 5]
res = [0] * len(arr)
cnt = 0
dfs(arr, 3)
print(cnt)
