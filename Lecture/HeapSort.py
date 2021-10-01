a = [7, 9, 4, 8, 6, 3]


def build_heap(a, n):
    for i in range(int(n/2), 1, -1):
        heapify(a, i, n)
        print(i)


def heap_sort(a, n):
    build_heap(a, n)
    for i in range(n, 2, -1):
        a[i], a[1] = a[1], a[i]
        heapify(a, 1, i-1)


def heapify(a, k, n):
    left = 2*k
    right = 2*k+1

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
        a[k] = a[smaller]
        heapify(a, smaller, n)


heap_sort(a, len(a)-1)
print(a)
