from algorithms.merge_sort import merge_sort


def is_sorted(nums):
    """Returns True if nums is sorted, False otherwise"""
    for i in range(1, len(nums)):
        if nums[i - 1] > nums[i]:
            return False
    return True


def test_basic():
    nums = [3, 8, 2, 5, 1, 4, 7, 6]
    merge_sort(nums)
    assert is_sorted(nums)


def test_negatives():
    nums = [-2, 3, 8, 2, -5, 12, 5, 1, 4, -7, 6, 0, 15, 7, 14, 13, -4]
    merge_sort(nums)
    assert is_sorted(nums)


def test_duplicates():
    nums = [1, 5, 2, 2, 4, 1, 1, 6, 5, 5, 5, 2]
    merge_sort(nums)
    assert is_sorted(nums)


def test_len_two():
    nums = [3, 1]
    merge_sort(nums)
    assert is_sorted(nums)


def test_len_one():
    nums = [7]
    merge_sort(nums)
    assert is_sorted(nums)


def test_empty():
    nums = []
    merge_sort(nums)
    assert is_sorted(nums)
