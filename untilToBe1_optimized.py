n, k = map(int, input().split())  # n,k값 입력받기
result = 0  # 횟수 저장용 변수

while True:
    temp = n//k
    remainder = n % k

    if n <= k:
        break

    n = temp
    result += 1+remainder

print(result)









