# 19 - Remove Nth Node From End of Linked List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
import random
import sys

from data_structures.linked_list_node import ListNode, list_to_ll
from leetcode.interfaces import Case, Solver, Suite

cases = [
    Case(
        name="Example 1",
        inputs=[list_to_ll([1, 2, 3, 4, 5]), 2],
        expected=list_to_ll([1, 2, 3, 5]),
    ),
    Case(
        name="Example 2",
        inputs=[list_to_ll([1]), 1],
        expected=list_to_ll([]),
    ),
    Case(
        name="Example 3",
        inputs=[list_to_ll([1, 2]), 1],
        expected=list_to_ll([1]),
    ),
    Case(
        name="Remove 1st Element",
        inputs=[list_to_ll([1, 2, 3, 4]), 4],
        expected=list_to_ll([2, 3, 4]),
    ),
]

# Add a large test case in order to compare runtime of two algorithms
size = 3_000
sys.setrecursionlimit(size * 10)
lst = [random.randint(1, size + 1) for _ in range(size)]
n = random.randint(1, size)
expected = lst.copy()
expected.pop(size - n)
large_test = Case(
    name="Large Input",
    inputs=[list_to_ll(lst), n],
    expected=list_to_ll(expected),
)
cases.append(large_test)


def two_pass(head: ListNode, n: int) -> ListNode:
    """
    Traverse the list to determine the length.
    Then, traverse the list again, stopping prior to the target node.

    Time: O(2 * length) = O(length)
    Space: O(1)
    """

    # Set up a sentinel node
    prehead = ListNode(0, head)

    # Traverse the list to find the length
    length = 0
    cur = prehead
    while cur.next:
        cur = cur.next
        length += 1

    # Take (length - n) steps from prehead to find target's predecessor
    cur = prehead
    for _ in range(length - n):
        cur = cur.next  # pyright: ignore[reportOptionalMemberAccess]

    # Remove target node
    cur.next = cur.next.next  # pyright: ignore[reportOptionalMemberAccess]

    # Return head of list using sentinel node
    return prehead.next  # pyright: ignore[reportReturnType]


def two_pointer(head: ListNode, n: int) -> ListNode:
    """
    Use two pointers, fast and slow, both starting at a sentinel prehead.
    Advance the fast pointer n times, so it is n steps ahead of slow.
    Now, advance both pointers one step at a time until fast.next = None.
    The slow pointer is now the predecessor to the target node.

    Time: O(length * 2) = O(length)
    Space: O(1)
    """

    # Set up a sentinel node and pointers
    prehead = ListNode(0, head)
    slow = fast = prehead

    # Start the fast pointer n steps ahead
    for _ in range(n):
        fast = fast.next  # pyright: ignore[reportOptionalMemberAccess]

    # Advance both pointers until the fast pointer is the last node
    while fast.next:  # pyright: ignore[reportOptionalMemberAccess]
        slow = slow.next  # pyright: ignore[reportOptionalMemberAccess]
        fast = fast.next  # pyright: ignore[reportOptionalMemberAccess]

    # Remove target node from linked list
    slow.next = slow.next.next  # pyright: ignore[reportOptionalMemberAccess]

    # Return head of list
    return prehead.next  # pyright: ignore[reportReturnType]


P0019_TEST_SUITE = Suite(
    number="p0019",
    name="Remove Nth Node From End of Linked List",
    solvers=[
        Solver("Two Pass", two_pass, ("Large Input",)),
        Solver("Two Pointer", two_pointer, ("Large Input",)),
    ],
    cases=cases,
)

if __name__ == "__main__":
    P0019_TEST_SUITE.run()
