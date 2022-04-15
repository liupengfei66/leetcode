def partition(a, l, r):
    x = a[r]
    i = l - 1
    for j in range(l, r):
        if a[j] < x:
            i += 1
            a[i], a[j] = a[j], a[i]
    i += 1
    a[i], a[r] = a[r], a[i]
    return i
arr = [6, 1, 2, 3, 5]
print(partition(arr, 0, 4))
print(arr)