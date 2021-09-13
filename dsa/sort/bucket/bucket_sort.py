from dsa.sort.insertion.insertion_sort import insertion_sort


def bucket_sort(arr: list[int], slot_count: int) -> None:
    aux = [[] for _ in range(slot_count)]

    for v in arr:
        index = int(v * slot_count)
        aux[index].append(v)

    for i in range(slot_count):
        insertion_sort(aux[i])

    k = 0
    for i in range(slot_count):
        for j in range(len(aux[i])):
            arr[k] = aux[i][j]
            k += 1
