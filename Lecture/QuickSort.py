a = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(a, p, r):
    if p < r:
        q = partition(a, p, r)
        quick_sort(a, p, q-1)
        quick_sort(a, q+1, r)


def partition(a, p, r):
    pivot = a[p]

    while True:
        for i in range(p+1, r):
            if a[i] > pivot:
                small_index = i
                break

        for j in range(r-1, p, -1):
            if a[j] < pivot:
                big_index = j
                break

        if big_index < small_index:
            a[p] = a[big_index]
            break

        else:
            a[big_index], a[small_index] = a[small_index], a[big_index]

    return big_index


print(quick_sort(a, 0, len(a)-1))
