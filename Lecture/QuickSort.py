a = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(a, p, r):
    # 파티션을 기준으로 왼쪽 오른쪽으로 반복 수행
    if p < r:
        q = partition(a, p, r)
        quick_sort(a, p, q-1)
        quick_sort(a, q+1, r)


def partition(a, p, r):
    pivot = p
    left = p + 1  # p는 pivot이라 +1부터 확인
    right = r

    # L, R이 엇갈리지 않을 때까지 반복
    while right >= left:
        # 엇갈리지 않는 선에서, pivot 보다 큰 값의 index 찾기 
        while left <= r and a[left] <= a[pivot]:
            left += 1
            
        # 엇갈리지 않는 선에서, pivot 보다 큰 값의 index 찾기
        while right > p and a[right] >= a[pivot]:
            right -= 1

        # 엇갈리면 pivot과 작은 값을 바꾸고, 작은 값이 있던 index 리턴
        if left > right:
            a[pivot], a[right] = a[right], a[pivot]
            return right

        # 엇갈리지 않았으면, 찾은 index의 원소를 뒤바꿔줌
        else:
            a[left], a[right] = a[right], a[left]


quick_sort(a, 0, len(a)-1)
print(a)
