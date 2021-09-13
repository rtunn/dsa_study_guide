def counting_sort(a, k):
    count = [0] * (k+1)
    output = [0] * len(a)

    for i in range(len(a)):
        v = a[i]
        count[v] += 1

    for i in range(1, k+1):
        count[i] += count[i - 1]

    for i in range(len(a)):
        t = len(a) - i - 1
        v = a[t]
        cv = count[v]
        output[cv - 1] = v
        count[v] -= 1

    for i in range(len(a)):
        a[i] = output[i]


# def counting_sort_while(a, k):
#     count = [0] * (k+1)

#     for i in range(len(a)):
#         v = a[i]
#         count[v] += 1

#     c = j = 0

#     while c < k + 1 and j < len(a):
#         while count[c] > 0:
#             a[j] = c
#             j += 1
#             count[c] -= 1
#         c += 1
