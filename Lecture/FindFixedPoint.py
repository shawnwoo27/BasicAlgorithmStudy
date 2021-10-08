n = int(input())
array = list(map(int, input().split()))


# (array, 0, n-1)
def binary_search(a, start, end):

    while True:
        mid = (start + end) // 2

        if a[mid] == mid:
            return mid

        elif a[mid] < mid:
            start = mid + 1
            binary_search(a, start, end)

        elif a[mid] > mid:
            end = mid - 1
            binary_search(a, start, end)

        elif start <= end:
            return -1


print(binary_search(array, 0, n-1))
