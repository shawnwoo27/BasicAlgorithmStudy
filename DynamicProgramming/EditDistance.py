def edit_dist(str1, str2):
    n = len(str1)
    m = len(str2)

    # (m+1) * (n+1) 크기의 테이블 생성
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dp[i][0] = i

    for j in range(1, m + 1):
        dp[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # 문자가 같다면 편집 거리 유지
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]

            else:  # 1 + min(삽입, 삭제, 교환)
                dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])

    return dp[n][m]


str1 = input()
str2 = input()

print(edit_dist(str1, str2))
