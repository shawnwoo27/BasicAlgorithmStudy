N, K = map(int, input().split())

dp = [0 for _ in range(K+1)]

for now in range(N):
    now_weight, now_value = map(int, input().split())

    for w in range(K, -1, -1):
        if now_weight <= w:
            dp[w] = max(dp[w], dp[w-now_weight] + now_value)

print(dp[K])
