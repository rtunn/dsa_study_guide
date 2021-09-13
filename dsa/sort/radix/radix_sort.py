def radix_sort(a, b=10):
    max1 = max(a)
    exp = 1
    while max1 / exp > 0:
        counting_sort(a, exp, b)
        exp *= b


def counting_sort(a, exp, b=10):
    count = [0] * b
    output = [0] * len(a)

    for i in range(len(a)):
        index = a[i] // exp
        count[index % b] += 1

    for i in range(1, b):
        count[i] += count[i - 1]

    j = len(a) - 1
    while j >= 0:
        index = a[j] // exp
        output[count[index % b] - 1] = a[j]
        count[index % b] -= 1
        j -= 1

    for i in range(len(a)):
        a[i] = output[i]
