n, k = map(int, input().split())  # n,k값 입력받기
result = 0  # 횟수 저장용 변수

while True:
    target = (n // k) * k
    result += (n - target)
    n = target

    if n < k:
        break

    n //= k
    result += 1

result += n-1
print(result)









