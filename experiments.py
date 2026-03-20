import random
from heapsort import heapsort, measure_time

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return quicksort(left) + [pivot] + quicksort(right)


def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left, right)


def merge(l, r):
    result = []
    i = j = 0
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1
    result.extend(l[i:])
    result.extend(r[j:])
    return result


sizes = [100, 500, 1000, 2000]

for size in sizes:
    arr = [random.randint(0, 10000) for _ in range(size)]

    print(f"\nSize {size}")
    print("HeapSort:", measure_time(heapsort, arr))
    print("QuickSort:", measure_time(quicksort, arr))
    print("MergeSort:", measure_time(mergesort, arr))