def quick_sort(a, l, h):
    if l >= h:
        return
    pivot = partition(a, l, h)
    quick_sort(a, l, pivot - 1)
    quick_sort(a, pivot + 1, h)


def partition(a, l, h):
    # for first index pivot
    # a[l], a[h] = a[h], a[l]

    # for midpoint pivot
    # m = l + (h - l) // 2
    # a[m], a[h] = a[h], a[m]

    # for random pivot
    # r = rand.randint(l, h)
    # a[r], a[h] = a[h], a[r]
    pivot = a[h]
    i = l
    for j in range(l, h):
        if a[j] < pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[h] = a[h], a[i]
    return i
