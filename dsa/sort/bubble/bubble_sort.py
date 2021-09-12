def bubble_sort(a):
    """"""
    while True:
        inversions = 0
        for i in range(0, len(a) - 1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                inversions += 1
        if inversions == 0:
            break
