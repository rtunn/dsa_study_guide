def quick_sort3(a, l, h):
    if l >= h:
        return
    p1, p2 = partition3(a, l, h)
    quick_sort3(a, l, p1 - 1)
    quick_sort3(a, p2 + 1, h)


def partition3(a, l, h):
    pivot = a[h]
    i = pl = l
    pr = h

    while i <= pr:
        if a[i] < pivot:
            a[i], a[pl] = a[pl], a[i]
            pl += 1
            i += 1
        elif a[i] > pivot:
            a[i], a[pr] = a[pr], a[i]
            pr -= 1
        else:
            i += 1
    return pl, pr
