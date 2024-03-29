import random
import copy
import time

tests = [random.sample(range(1, 10 ** 3), 10 ** 2),
         random.sample(range(1, 10 ** 8), 10 ** 2),
         random.sample(range(1, 10 ** 4), 10 ** 3),
         random.sample(range(1, 10 ** 6), 10 ** 3),
         random.sample(range(1, 10 ** 7), 10 ** 5),
         random.sample(range(1, 10 ** 8), 10 ** 6),
         random.sample(range(1, 10 ** 9), 10 ** 7)]

tests_copy = copy.deepcopy(tests)


def test_sort(v):
    n = len(v)
    for i in range(1, n):
        if v[i] < v[i - 1]:
            return False
    return True


def radix_sort(v, cif):
    for k in range(0, cif):
        buck = [[] for p in range(10)]
        for x in v:
            buck[(x // (10 ** k)) % 10].append(x)
        index = 0
        for i in range(0, 10):
            for j in range(0, len(buck[i])):
                v[index] = buck[i][j]
                index += 1
    return v


def radix_sort_2to16(v):
    for k in range(0, 64, 16):
        buck = [[] for p in range(65536)]
        for x in v:
            buck[(x >> k) & 65535].append(x)
        index = 0
        for i in range(0, 65536):
            for j in range(0, len(buck[i])):
                v[index] = buck[i][j]
                index += 1
    return v


def merge(lst, ldr):
    i = j = 0
    res = []
    while i < len(lst) and j < len(ldr):
        if lst[i] < ldr[j]:
            res.append(lst[i])
            i += 1
        else:
            res.append(ldr[j])
            j += 1
    res.extend(lst[i:])
    res.extend(ldr[j:])
    return res


def merge_sort(v):
    if len(v) <= 1:
        return v
    else:
        mij = len(v) // 2
        lst = merge_sort(v[:mij])
        ldr = merge_sort(v[mij:])
        return merge(lst, ldr)


def shell_sort(v):
    n = len(v)
    gap = 1
    while gap < n // 3:
        gap = gap * 3 + 1
    while gap >= 1:
        for i in range(gap, n):
            current = v[i]
            j = i
            while j >= gap and v[j - gap] > current:
                v[j] = v[j - gap]
                j -= gap
            v[j] = current
        gap //= 3
    return v


def pivot_mediana_din_3(x, y, z):
    if y <= x <= z or z <= x <= y:
        return x
    if x <= y <= z or z <= y <= x:
        return y
    return z


def quick_sort(v):
    if len(v) <= 1:
        return v
    else:
        if len(v) >= 3:
            pivot = pivot_mediana_din_3(v[0], v[len(v) // 2], v[len(v) - 1])
        else:
            pivot = v[0] if v[0] >= v[1] else v[1]
        L = [x for x in v if x < pivot]
        E = [x for x in v if x == pivot]
        G = [x for x in v if x > pivot]
        return quick_sort(L) + E + quick_sort(G)


def heapify(array, index, length):
    max = index
    left = 2 * index + 1
    right = 2 * index + 2

    if left < length and array[max] < array[left]:
        array[left], array[max] = array[max], array[left]
        heapify(array, left, length)

    if right < length and array[max] < array[right]:
        array[right], array[max] = array[max], array[right]
        heapify(array, right, length)


def heap_sort(array):
    if len(array) > 5000:
        return
    for index in range(len(array) - 1, -1, -1):
        heapify(array, index, len(array))
    for index in range(len(array) - 1, 0, -1):
        array[index], array[0] = array[0], array[index]
        heapify(array, 0, index)


def sort_and_measure(sorting_alg, tests):
    for v in tests:
        if sorting_alg.__name__ == 'radix_sort':
            max_val = max(v)
            num_digits = len(str(max_val))
            start_time = time.time()
            sorting_alg(v, num_digits)
            end_time = time.time()
        else:
            start_time = time.time()
            sorting_alg(v)
            end_time = time.time()
        sort_time = round((end_time - start_time), 4)
        if sort_time > 59:
            print("\033[91m" + "Limit time exceeded!" + "\033[0m")
            return
        elif sort_time < 59 and test_sort(v):
            print(f"{sorting_alg.__name__} took {sort_time:.4f} seconds")


if __name__ == '__main__':
    for sorting_alg in [radix_sort, radix_sort_2to16, merge_sort, shell_sort, quick_sort, heap_sort]:
        sort_and_measure(sorting_alg, tests_copy)
