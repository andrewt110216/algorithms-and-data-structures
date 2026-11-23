# 020 - Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/

from collections import deque

from leetcode.interfaces import Case, Solver, Suite

cases = [
    Case(
        name="Example 1",
        inputs=["()"],
        expected=True,
    ),
    Case(
        name="Example 2",
        inputs=["()[]{}"],
        expected=True,
    ),
    Case(
        name="Example 3",
        inputs=["(]"],
        expected=False,
    ),
    Case(
        name="Single Bracket",
        inputs=["]"],
        expected=False,
    ),
    Case(
        name="Nested Example - Valid",
        inputs=["([{()}])"],
        expected=True,
    ),
    Case(
        name="Nested Example - Invalid",
        inputs=["([{()}[])"],
        expected=False,
    ),
]


def stack(s: str) -> bool:
    """
    Use a LIFO stack: add open brackets to the stack and when a closed bracket
    is encountered, pop from the stack and check that these two brackets match.

    Specifically, we use a deque (double ended queue) in Python as it
    guarantees O(1) append/pop, whereas a list may be O(n) due to the need to
    resize the list and call realloc, copying all items in the list to the new
    memory.

    Time: O(n) (iterate over s once)
    Space: O(n) (max length of the stack, if no closing brackets)
    """
    opening = ["(", "[", "{"]
    closing = [")", "]", "}"]
    stack = deque()
    for char in s:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack:
                return False  # invalid closing bracket
            open = stack.pop()
            if closing.index(char) != opening.index(open):
                return False  # non-matching opening bracket
        else:
            return False  # invalid character
    if stack:
        return False  # unclosed open bracket found
    return True


P0020_TEST_SUITE = Suite(
    number="p0020",
    name="Valid Parentheses",
    solvers=[Solver(name="Stack", fn=stack)],
    cases=cases,
)


if __name__ == "__main__":
    P0020_TEST_SUITE.run()
