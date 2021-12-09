str1 = list(input())
str2 = list(input())

str1_len = len(str1)
str2_len = len(str2)

dp = [[0] * (str2_len + 1) for i in range(str1_len + 1)]

for i in range(str1_len):
    for j in range(str2_len):
        if str1[i] == str2[j]:
            dp[i + 1][j + 1] = dp[i][j] + 1
        else:
            dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

print(dp[str1_len][str2_len])
