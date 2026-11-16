"""
003 - Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""

from leetcode.interfaces import Case, Solver, Suite

cases = [
    Case(
        name="Example 1",
        inputs=["abcabcbb"],
        expected=3,
    ),
    Case(
        name="Example 2",
        inputs=["bbbbb"],
        expected=1,
    ),
    Case(
        name="Example 3",
        inputs=["pwwkew"],
        expected=3,
    ),
    Case(
        name="Empty String",
        inputs=[""],
        expected=0,
    ),
    Case(
        name="Repeats Only at Start",
        inputs=["aabcdef"],
        expected=6,
    ),
    Case(
        name="Repeats Only at End",
        inputs=["abcdeff"],
        expected=6,
    ),
    Case(
        name="Multiple Repeats",
        inputs=["aabcdaebefga"],
        expected=5,  # 'bcdae', 'cdaeb', 'befga'
    ),
    Case(
        name="Ensure No Slide Backwards",
        inputs=["ccbbcc"],
        expected=2,
    ),
]


def sliding_window(s: str) -> int:
    """
    Use a sliding window with two pointers, optimized by saving the highest
    index where each character is found in a dictionary so that the left
    pointer can jump ahead when repeat characters are encountered.

    Time: O(n) (one pass through s)
    Space: O(1) (max size of the dictionary)
        There is a limited number of possible characters (per the problem
        description) so the space is O(1) not O(n).
    """
    max_len = 0
    char_to_last_seen_idx = {}
    left = 0
    for right, char in enumerate(s):
        # Only move left forward, never backwards.
        if (
            char in char_to_last_seen_idx
            and char_to_last_seen_idx[char] >= left
        ):
            left = char_to_last_seen_idx[char] + 1
        max_len = max(max_len, right - left + 1)
        char_to_last_seen_idx[char] = right
    return max_len


def brute_force(s: str) -> int:
    """
    Check each substring of non-repeating characters (storing seen characters
    in a set), and dynamically update the maximum length.

    Time: O(n^2)
    Space: O(n) (max size of the set)
    """
    n = len(s)
    if n == 0:
        return 0

    seen = set()
    cur_len = 1  # length of current substring
    max_len = 1  # maximum substring length

    # Left pointer will slide from 0 to n - 1
    left = 0
    while left < n - 1:
        seen.add(s[left])

        # right pointer will slide from 1 to last element
        right = left + 1
        while right < n:
            char = s[right]
            if char not in seen:
                cur_len += 1
                max_len = max(max_len, cur_len)
                seen.add(char)
                right += 1
            else:
                break

        # restart sliding window with next character
        left += 1
        seen.clear()
        cur_len = 1

    return max_len


P0003_TEST_SUITE = Suite(
    number="p0003",
    name="Longest Substring Without Repeats",
    solvers=[
        Solver(
            name="Sliding Window",
            fn=sliding_window,
        ),
        Solver(
            name="Brute Force",
            fn=brute_force,
        ),
    ],
    cases=cases,
)


if __name__ == "__main__":
    P0003_TEST_SUITE.run()
