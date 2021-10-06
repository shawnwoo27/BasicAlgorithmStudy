a = [7, 9, 4, 8, 6, 3]


def build_heap(a, n):
    for i in range(n//2, 0, -1):
        heapify(a, i, n)


def heap_sort(a, n):
    build_heap(a, n)
    for i in range(n, 0, -1):
        a[0], a[i] = a[i], a[0]
        heapify(a, 0, i-1)


def heapify(a, k, n):
    left = 2*k + 1
    right = 2*k + 2

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
print(a)
