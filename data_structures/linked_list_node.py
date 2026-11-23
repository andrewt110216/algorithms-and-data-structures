"""
Singly-linked list node.
"""

from __future__ import annotations


class ListNode:
    """
    A node of a singly-linked list.
    """

    def __init__(
        self, val: int = 0, next: ListNode | None = None, has_cycle=False
    ):
        self.val = val
        self.next = next
        self.has_cycle = has_cycle

    def __repr__(self):
        val = self.next.val if self.next else "None"
        return f"<ListNode {self.val} -> " f"({val})>"

    def __str__(self):
        return self.__repr__()

    def __eq__(self, node2):
        """Two ListNodes are equal if their list representations are equal"""
        if not isinstance(node2, ListNode):
            return NotImplemented
        return ll_to_list(self) == ll_to_list(node2)


def list_to_ll(array: list[int]) -> ListNode | None:
    """
    Convert a list to a linked list of ListNodes
    """
    n = len(array)
    if n == 0:
        return None
    head = ListNode(array[0])
    prev = head
    i = 1
    while i < n:
        new_node = ListNode(array[i])
        prev.next = new_node
        prev = prev.next
        i += 1
    return head


def ll_to_list(head: ListNode) -> list[int]:
    """
    Convert a linked list to a traditional list
    """
    array = []
    if head:
        cur = head
        while cur and cur.next:
            array.append(cur.val)
            cur = cur.next
        array.append(cur.val)
    return array
