a = [7, 9, 4, 8, 6, 3]


def build_heap(a, n):
    # 마지막 인덱스의 부모 노드 부터 heapify 시작
    for i in range(n//2, -1, -1):
        heapify(a, i, n)


def heap_sort(a, n):
    build_heap(a, n)

    # 최상위 노드 값이 가장 작으므로
    # 최상위 노드를 출력 후, 맨끝 값하고 바꾸고
    # heapify 를 통해 최상위 노드가 항상 가장 작은 상태를 유지
    for i in range(n, -1, -1):
        print(a[0])
        a[0], a[i] = a[i], a[0]
        heapify(a, 0, i-1)


def heapify(a, k, n):
    left = 2*k + 1  # 왼쪽 자식 노드
    right = 2*k + 2  # 오른쪽 자식 노드

    if right <= n:
        if a[left] < a[right]:
            smaller = left
        else:
            smaller = right

    elif left <= n:
        smaller = left

    else:
        return

    if a[smaller] < a[k]:
        a[k], a[smaller] = a[smaller], a[k]
        heapify(a, smaller, n)


heap_sort(a, len(a)-1)

