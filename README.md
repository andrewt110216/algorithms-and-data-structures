# Algorithms & Data Structures

<em>Python files for Algorithms & Data Structures and Leetcode solutions</em>

![GitHub Workflow Results - Tests & Linting](https://github.com/andrewt110216/algorithms-and-data-structures/actions/workflows/tests.yml/badge.svg) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

<!-- THESE 3 BADGE VALUES ARE HARD CODED -->
![LC Problems](https://img.shields.io/badge/LC%20Problems-34-orange) ![Algorithms](https://img.shields.io/badge/Algorithms-3-red) ![Data Structures](https://img.shields.io/badge/Data%20Structures-4-blue)

# Development

Created virtual environment with:
```
uv venv env --python 3.14
```

Activate and install deps:
```
source env/bin/activate
uv pip install -e ".[dev]"
```

Update deps:
```
uv pip freeze --exclude-editable --python env/bin/python > requirements.txt
```

# Run

Print test case results for a single problem:
```
python -m leetcode.main p0001
```

Test all cases across all files:
```
pytest -v leetcode
```

## Algorithms

| Count | Migrated | Algorithm |
| --- | --- | --- |
| 1 | ❌ | [QuickSort](algorithms/quick_sort.py) |
| 2 | ❌ | [MergeSort](algorithms/merge_sort.py) |
| 3 | ❌ | [Kosaraju](algorithms/kosaraju.py) |

## Data Structures

| Count | Migrated | Data Structure |
| --- | --- | --- |
| 1 | ❌ | [Linked List](data_structures/linked_list.py) |
| 2 | ❌ | [Binary Tree](data_structures/binary_tree_node.py) |
| 3 | ❌ | [Heap](data_structures/heap.py) |
| 4 | ❌ | [LRU Cache](data_structures/lru_cache.py)


## Leetcode

| Count | LC # | Migrated | Description | Difficulty |
| --- | --- | --- | --- | --- |
| 1 | 1 | ✅ | [Two Sum](leetcode/p0001.py) | Easy |
| 2 | 3 | ❌ | [Longest Substring Without Repeating Characters](leetcode/p0003_solution.py) | Medium |
| 3 | 19 | ❌ |  [Remove Nth Node From Linked List](leetcode/p0019_solution.py) | Medium |
| 4 | 20 | ❌ |  [Valid Parentheses](leetcode/p0020_solution.py) | Easy |
| 5 | 21 | ❌ |  [Merge Two Sorted Linked Lists](leetcode/p0021_solution.py) | Easy |
| 6 | 34 | ❌ |  [Find First and Last Position of Element in Sorted Array](leetcode/p0034_solution.py) | Medium |
| 7 | 46 | ❌ | [Permutations](leetcode/p0046_solution.py) | Medium |
| 8 | 53 | ❌ | [Maximum Subarray](leetcode/p0053_solution.py) | Medium |
| 9 | 70 | ❌ | [Climbing Stairs](leetcode/p0070_solution.py) | Easy |
| 10 | 77 |  ❌ | [Combinations](leetcode/p0077_solution.py) | Medium |
| 11 | 120 | ❌ | [Triangle](leetcode/p0120_solution.py) | Medium |
| 12 | 141 | ❌ | [Linked List Cycle](leetcode/p0141_solution.py) | Easy |
| 13 | 148 | ❌ | [Sort List](leetcode/p0148_solution.py) | Medium |
| 14 | 189 | ❌ | [Rotate Array](leetcode/p0189_solution.py) | Medium |
| 15 | 198 | ❌ | [House Robber](leetcode/p0198_solution.py) | Medium |
| 16 | 200 | ❌ | [Number of Islands](leetcode/p0200_solution.py) | Medium |
| 17 | 203 | ❌ | [Remove Linked List Elements](leetcode/p0203_solution.py) | Easy |
| 18 | 215 | ❌ | [Kth Largest Element in an Array](leetcode/p0215_solution.py) | Medium |
| 19 | 283 | ❌ | [Move Zeroes](leetcode/p0283_solution.py) | Easy |
| 20 | 286 | ❌ | [Walls and Gates](leetcode/p0286_solution.py) | Medium |
| 21 | 344 | ❌ | [Reverse String](leetcode/p0344_solution.py) | Easy |
| 22 | 347 | ❌ | [Top K Frequent Items](leetcode/p0347_solution.py) | Medium |
| 23 | 542 | ❌ | [01 Matrix](leetcode/p0542_solution.py) | Medium |
| 24 | 617 | ❌ | [Merge Two Binary Trees](leetcode/p0617_solution.py) | Easy |
| 25 | 695 | ❌ | [Max Area of Island](leetcode/p0695_solution.py) | Medium |
| 26 | 704 | ❌ | [Binary Search](leetcode/p0704_solution.py) | Easy |
| 27 | 707 | ❌ | [Design Linked List](leetcode/p0707_solution.py) | Medium |
| 28 | 733 | ❌ | [Flood Fill](leetcode/p0733_solution.py) | Easy |
| 29 | 784 | ❌ | [Letter Case Permutation](leetcode/p0784_solution.py) | Easy |
| 30 | 931 | ❌ | [Minimum Falling Path Sum](leetcode/p0931_solution.py) | Medium |
| 31 | 977 | ❌ | [Squares of a Sorted Array](leetcode/p0977_solution.py) | Easy |
| 32 | 994 | ❌ | [Rotting Oranges](leetcode/p0994_solution.py) | Medium |
| 33 | 1006 | ❌ | [Clumsy Factorial](leetcode/p1006_solution.py) | Medium |
| 34 | 1029 | ❌ | [Two City Scheduling](leetcode/p1029_solution.py) | Medium |
