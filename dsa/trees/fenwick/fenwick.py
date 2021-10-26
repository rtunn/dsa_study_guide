class Fenwick:

    def __init__(self, bound: int):
        self.bound = bound
        self.size = bound + 1
        self.arr = [0 for _ in range(self.size)]

    def add(self, idx: int, val: int) -> None:
        idx += 1
        while idx < self.size:
            self.arr[idx] += val
            idx += idx & -idx

    def sum(self, idx: int) -> int:
        idx += 1
        res = 0
        while idx > 0:
            res += self.arr[idx]
            idx -= idx & -idx
        return res

    def query(self, start: int, end: int) -> int:
        return self.sum(end) - self.sum(start)

    def prefix(self, end: int) -> int:
        return self.sum(end)

    def suffix(self, start: int) -> int:
        return self.sum(self.bound - 1) - self.sum(start - 1)


# Find the Number of Increasing/Decreasing Sequences in a List
def num_sequences(items: list[int], bound: int) -> int:
    left_bit = Fenwick(bound)
    right_bit = Fenwick(bound)

    for item in items:
        right_bit.add(item, 1)

    num_increasing = 0
    num_decreasing = 0
    for item in items:
        right_bit.add(item, -1)
        num_increasing += left_bit.prefix(item) * right_bit.suffix(item)
        num_decreasing += left_bit.suffix(item) * right_bit.prefix(item)
        left_bit.add(item, 1)
    return num_increasing, num_decreasing


def main():
    k = int(input())
    items = []
    for _ in range(k):
        items.append(int(input()))
    bound = int(input())
    print(num_sequences(items, bound))


if __name__ == '__main__':
    main()
