````
# Assignment 4: Heap Data Structures – Implementation, Analysis, and Applications

## 1. Introduction
This assignment focuses on understanding **heap data structures**, implementing **Heapsort**, and building a **priority queue**. The goal is to analyze the efficiency of heap-based algorithms compared to other sorting algorithms such as QuickSort and MergeSort and to explore practical applications of priority queues.

---

## 2. Heap Theory

A **heap** is a complete binary tree that satisfies the **heap property**:

- **Max Heap:** Each parent node is greater than or equal to its children.
- **Min Heap:** Each parent node is less than or equal to its children.

Heaps are commonly implemented using arrays where:

- Left child index: `2*i + 1`
- Right child index: `2*i + 2`
- Parent index: `(i - 1) // 2`

Heaps allow efficient **priority-based operations** like insertion, extraction, and key modification, which are essential for tasks such as **task scheduling** and **graph algorithms**.

---

## 3. Heapsort Algorithm

**Heapsort Steps:**

1. Build a **max heap** from the input array.
2. Swap the root with the last element and reduce heap size.
3. Heapify the root to maintain the heap property.
4. Repeat until the heap is empty.

**Time Complexity:**

- Building the heap: `O(n)`
- Extracting elements and heapifying: `O(n log n)`
- **Overall:** `O(n log n)` in best, average, and worst cases

**Space Complexity:** `O(1)` (in-place sorting)

---

## 4. Priority Queue Implementation

A **priority queue** is a data structure where each element has a priority. Elements with higher priorities are dequeued before lower-priority elements.

**Implemented Operations & Complexities:**

| Operation          | Complexity |
|-------------------|------------|
| Insert             | O(log n)   |
| Extract Max        | O(log n)   |
| Increase Priority  | O(log n)   |
| Peek Max           | O(1)       |

**Task Example:**

```python
Task(id=1, priority=10, arrival_time=0, deadline=5)
````

Priority queues are useful for:

- **Task scheduling** in operating systems
- **Real-time systems**
- **Graph algorithms** (e.g., Dijkstra's algorithm, Prim's algorithm)

---

## 5. Experimental Setup

Sorting algorithms were tested on randomly generated arrays of sizes `[100, 500, 1000, 2000]`.

Implemented algorithms:

- **HeapSort** (using max heap)
- **QuickSort** (recursive, first element pivot)
- **MergeSort** (divide and conquer)

**Python function used to measure execution time:**

```python
def measure_time(func, arr):
    start = time.time()
    func(arr.copy())
    return time.time() - start
```

---

## 6. Results

| Array Size | HeapSort (s) | QuickSort (s) | MergeSort (s) |
| ---------- | ------------ | ------------- | ------------- |
| 100        | 0.000107     | 0.000069      | 0.000098      |
| 500        | 0.000715     | 0.000414      | 0.000572      |
| 1000       | 0.001635     | 0.001017      | 0.001328      |
| 2000       | 0.003586     | 0.002030      | 0.002467      |

---

## 7. Analysis

1. **QuickSort** is consistently the fastest on these random datasets due to low overhead and good cache performance. Its **average-case complexity** is `O(n log n)`.

2. **HeapSort** is slightly slower because each extraction requires **heapify operations**, which involve multiple swaps. However, it has the advantage of guaranteed `O(n log n)` performance even in the worst case.

3. **MergeSort** performs well but involves additional memory allocation for merging, slightly increasing runtime.

4. **Scaling:** All three algorithms demonstrate roughly `O(n log n)` behavior as array size increases, consistent with theoretical expectations.

---

## 8. Conclusion

- **HeapSort** is a reliable, in-place, comparison-based sorting algorithm with predictable `O(n log n)` performance.
- **Priority queues** efficiently manage elements based on priority, with logarithmic-time insertions and extractions.
- Experimental results confirm theoretical time complexities and highlight practical differences among HeapSort, QuickSort, and MergeSort.
- Using heaps for priority queues provides a foundation for applications in task scheduling and graph-based algorithms.
