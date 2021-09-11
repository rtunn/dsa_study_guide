def merge_sort(a, l, h):
    if l >= h:
        return

    m = l + (h - l) // 2

    merge_sort(a, l, m)
    merge_sort(a, m+1, h)

    merge(a, l, m, h)


def merge(a, l, m, h):
    i = l
    j = m + 1
    aux = []

    while i <= m and j <= h:
        if a[i] > a[j]:
            aux.append(a[j])
            j += 1
        else:
            aux.append(a[i])
            i += 1

    while i <= m:
        aux.append(a[i])
        i += 1

    while j <= h:
        aux.append(a[j])
        j += 1

    a[l:h + 1] = aux
