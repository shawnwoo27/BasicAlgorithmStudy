n, k = map(int, input().split())  # n,k값 입력받기
num = 0  # 횟수 저장용 변수

while k > n:
    n, k = map(int, input().split())  # k가 n보다 크면 다시 입력

while n >= k:  # n이 k보다 크면 계속 나누기

    while n % k > 0:  # 나뉘어 떨어지지 않으면 1번 과정 수행
        n -= 1
        num += 1

    n //= k
    num += 1
    
print(num)









