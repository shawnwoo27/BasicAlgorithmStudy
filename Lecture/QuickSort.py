a = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(a, p, r):
    if p < r:
        q = partition(a, p, r)
        quick_sort(a, p, q-1)
        quick_sort(a, q+1, r)


def partition(a, p, r):
    pivot = p
    left = p + 1
    right = r

    while right >= left:
        while left <= r and a[left] <= a[pivot]:
            left += 1

        while right > p and a[right] >= a[pivot]:
            right -= 1

        if left > right:
            a[pivot], a[right] = a[right], a[pivot]
            return right

        else:
            a[left], a[right] = a[right], a[left]


quick_sort(a, 0, len(a)-1)
print(a)
