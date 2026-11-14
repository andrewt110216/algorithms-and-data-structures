"""
0001 - Two Sum
https://leetcode.com/problems/two-sum/
"""

from leetcode.interfaces import Case, NoSolutionError, Solver, Suite

cases = [
    Case(
        name="Example 1",
        inputs=[[2, 7, 11, 15], 9],
        expected=[0, 1],
    ),
    Case(
        name="Example 2",
        inputs=[[3, 2, 4], 6],
        expected=[1, 2],
    ),
    Case(
        name="Example 3",
        inputs=[[3, 3], 6],
        expected=[0, 1],
    ),
    Case(
        name="Large Input",
        inputs=[list(range(10_001)), 19_999],
        expected=[9_999, 10_000],
    ),
    Case(
        name="No Solution",
        inputs=[[1, 2, 3, 4, 5], 10],
        expected=NoSolutionError(),
    ),
]


def two_sum_hash_map(nums: list[int], target: int) -> list[int]:
    """
    Hash map, saving seen elements in a dictionary during the
    single pass through the list.

    Time: O(n)
    Space: O(n)
    """
    seen: dict[int, int] = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    raise NoSolutionError()


def two_sum_brute(nums: list[int], target: int) -> list[int]:
    """
    Brute force, iterative solution, using nested for loop to evaluate
    every pair of elements in nums.

    Time: O(n^2) (n = 50,000 => runtime ~1 minute)
    Space: O(1)
    """
    n = len(nums)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    raise NoSolutionError()


P0001_TEST_SUITE = Suite(
    number="p0001",
    name="Two Sum",
    solvers=[Solver("Hash Map", two_sum_hash_map)],
    cases=cases,
)


if __name__ == "__main__":
    P0001_TEST_SUITE.run()
