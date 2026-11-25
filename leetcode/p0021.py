# 020 - Merge Two Sorted (Linked) Lists
# https://leetcode.com/problems/merge-two-sorted-lists/

from data_structures.linked_list_node import ListNode, list_to_ll
from leetcode.interfaces import Case, Solver, Suite

cases = [
    Case(
        name="Example 1",
        inputs=list(map(list_to_ll, [[1, 2, 4], [1, 3, 4]])),
        expected=list_to_ll([1, 1, 2, 3, 4, 4]),
    ),
    Case(
        name="Example 2",
        inputs=list(map(list_to_ll, [[], []])),
        expected=list_to_ll([]),
    ),
    Case(
        name="Example 3",
        inputs=list(map(list_to_ll, [[], [0]])),
        expected=list_to_ll([0]),
    ),
    Case(
        name="Add Duplicates and Negatives",
        inputs=list(map(list_to_ll, [[-2, 0, 1, 4, 4], [-8, -2, -1, 0, 3]])),
        expected=list_to_ll([-8, -2, -2, -1, 0, 0, 1, 3, 4, 4]),
    ),
]


def recursive(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
    """
    Build the merged list recursively. Create a new `merged` list and set
    the value of the head node to the smaller of l1.val and l2.val. Advance
    the pointers for l1 or l2, and repeat recursively on `merged.next` to
    build the rest of the merged list

    Time: O(n + m) (one recursive call per element in each list)
    Space: O(n + m) (the call stack)
    """

    def recurse(l1: ListNode | None, l2: ListNode | None):

        # base case: one or both nodes are null

        # if l1 is null, the rest of l2 needs to be merged or, in the case that
        # l2 is also null, we set the next pointer of the final node of merged
        # to null (l2)
        if l1 is None:
            return l2

        # if l2 is null, the rest of l1 needs to be merged
        if l2 is None:
            return l1

        # `head` is the head of the output list and `merged` is the pointer
        head = ListNode()
        merged = head

        # set the value of merged to the smaller of l1 and l2 and advance
        # that list to the next node
        if l1.val < l2.val:
            merged.val = l1.val
            l1 = l1.next
        else:
            merged.val = l2.val
            l2 = l2.next

        # set merged.next by recursing on the rest of l1 and l2
        merged.next = recurse(l1, l2)

        # return the head of our output list
        return head

    return recurse(l1, l2)


def iterative(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
    """
    This is the merge subroutine of the merge-sort algorithm.

    Traverse l1 and l2, copying the smaller node into merged, then advance
    that list and merged. When one of l1 or l2 is exhausted, copy over the
    remaining nodes from the other list

    Time: O(n + m) (one recursive call per element in each list)
    Space: O(1) (no additional data strucutre or call stack needed)
    """

    # check for empty input
    if l1 is None and l2 is None:
        return None

    # `head` is the head of the output list and `merged` is the pointer
    head = ListNode()
    merged = head

    # traverse both lists, copying smaller node into `merged`
    while l1 and l2:
        if l1.val < l2.val:
            merged.val = l1.val
            l1 = l1.next
        else:
            merged.val = l2.val
            l2 = l2.next

        # advance merged to next node, if necessary
        if l1 or l2:
            merged.next = ListNode()
            merged = merged.next

    # copy remaining nodes from l1 or l2 into merged
    while l1:
        merged.val = l1.val
        l1 = l1.next
        if l1:
            merged.next = ListNode()
            merged = merged.next
    while l2:
        merged.val = l2.val
        l2 = l2.next
        if l2:
            merged.next = ListNode()
            merged = merged.next

    return head


P0021_TEST_SUITE = Suite(
    number="p0021",
    name="Merge Linked Lists",
    solvers=[
        Solver(name="Recursive", fn=recursive),
        Solver(name="Iterative", fn=iterative),
    ],
    cases=cases,
)


if __name__ == "__main__":
    P0021_TEST_SUITE.run()
