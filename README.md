# Assignment 4: Heap Data Structures

## Overview

This project implements **HeapSort** and a **Priority Queue** using Python. It includes experiments comparing HeapSort with QuickSort and MergeSort and demonstrates practical applications of heaps in task scheduling.

---

## Repository Structure

```

assignment-4-heaps/
│── heapsort.py           # HeapSort implementation & timing functions
│── priority_queue.py     # Priority Queue implementation
│── experiments.py        # Sorting experiments & timing comparison
│── report.md             # Detailed report with analysis and results
│── README.md             # Project overview and instructions

```

---

## How to Run

1. Clone the repository.
2. Ensure Python 3 is installed.
3. Run experiments to compare sorting algorithms:

```bash
python3 experiments.py
```

The output will display execution times for HeapSort, QuickSort, and MergeSort on arrays of different sizes.

---

## Algorithm Comparison

| Algorithm | Best Case  | Average Case | Worst Case | Notes                                    |
| --------- | ---------- | ------------ | ---------- | ---------------------------------------- |
| HeapSort  | O(n log n) | O(n log n)   | O(n log n) | Consistent performance                   |
| QuickSort | O(n log n) | O(n log n)   | O(n^2)     | Fast in practice, average case efficient |
| MergeSort | O(n log n) | O(n log n)   | O(n log n) | Requires extra memory for merging        |

---

## Priority Queue

The `PriorityQueue` class supports:

- `insert(task)`: Add a new task with priority
- `extract_max()`: Remove the task with the highest priority
- `increase_priority(task_id, new_priority)`: Update task priority
- `is_empty()`: Check if queue is empty

**Complexities:** O(log n) for insert, extract, and increase key.

**Example Usage:**

```python
from priority_queue import Task, PriorityQueue

pq = PriorityQueue()
pq.insert(Task(1, 10, 0, 5))
pq.insert(Task(2, 5, 1, 3))

top_task = pq.extract_max()
print(top_task)  # Task(id=1, priority=10)
```

---

## Author

**Shreya Rai**
M.S. in Computer Science
GitHub: https://github.com/ShreyaRai20/assignment-4-heaps.git
