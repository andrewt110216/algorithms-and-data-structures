"""
An API to represent a Singly-Linked List of integers and provide basic
operations, including insert, delete, search, and sort
"""

from __future__ import annotations
from data_structures.linked_list_node import ListNode
from functools import wraps
from typing import Callable, Concatenate


class CycleException(Exception):
    pass


def _no_cycle[**P, R](
    f: Callable[Concatenate[LinkedList, P], R],
) -> Callable[Concatenate[LinkedList, P], R]:
    """
    Raise CycleException instead of running f on a list with a cycle.
    """

    @wraps(f)
    def wrapped(self: LinkedList, *args: P.args, **kwargs: P.kwargs) -> R:
        if self.has_cycle():
            msg = f'Cannot run "{f.__name__}" on a list with a cycle'
            raise CycleException(msg)
        return f(self, *args, **kwargs)

    return wrapped


class LinkedList:
    """
    Represent a singly-linked list

    While it is discouraged, LinkedList allows cycles. However, most operations
    are disallowed on a list with a cycle to prevent infinite loops.
    """

    def __init__(self, node_values: list[int] = []):
        self._prehead = ListNode()
        self._tail = None
        self._length = 0
        if node_values:
            self.from_array(node_values)

    @_no_cycle
    def __len__(self):
        return self._length

    @_no_cycle
    def __eq__(self, list2):
        """Compare self to another linked list for equality"""
        if type(list2) != LinkedList:
            return False
        cur1 = self.get_head()
        cur2 = list2.get_head()
        while cur1 and cur2:
            if cur1.val != cur2.val:
                return False
            cur1 = cur1.next
            cur2 = cur2.next
        if cur1 or cur2:
            return False
        return True

    def is_empty(self):
        """Return self._length == 0"""
        return self._length == 0

    def get_head(self):
        """Return head node"""
        return self._prehead.next

    def get_tail(self):
        """Return tail node"""
        return self._tail

    @_no_cycle
    def insert(self, index: int, value: int):
        """Insert a new node at index"""
        if index < 0 or index > self._length:
            raise IndexError
        cur = 0
        prev = self._prehead
        while cur <= self._length and prev:
            if cur == index:
                new_node = ListNode(value)
                tmp = prev.next
                prev.next = new_node
                new_node.next = tmp
                self._length += 1
                if cur == self._length - 1:
                    self._tail = new_node
                break
            prev = prev.next
            cur += 1

    @_no_cycle
    def from_array(self, items: list[int]):
        """Add items from array to end of list"""
        prev = self._tail if self._tail else self._prehead
        for item in items:
            new_node = ListNode(item)
            prev.next = new_node
            prev = new_node
        self._length += len(items)
        self._tail = prev

    @_no_cycle
    def get_value(self, index: int) -> int:
        """Return value of node at index"""
        if not 0 <= index < self._length:
            raise IndexError
        cur = self.get_head()
        for _ in range(index):
            cur = cur.next
        return cur.val

    @_no_cycle
    def find_value(self, target: int) -> int:
        """Return index of first occurence of target value in self"""
        cur_idx = 0
        cur = self.get_head()
        while cur:
            if cur.val == target:
                return cur_idx
            cur = cur.next
            cur_idx += 1
        raise ValueError

    @_no_cycle
    def count(self, target: int) -> int:
        """Count number of ocurrences of target value in self"""
        count = 0
        cur = self.get_head()
        while cur:
            if cur.val == target:
                count += 1
            cur = cur.next
        return count

    @_no_cycle
    def find_all(self, target: int) -> list:
        """Return indices of all occurences of target value in self"""
        indices = []
        cur_idx = 0
        cur = self._prehead.next
        while cur:
            if cur.val == target:
                indices.append(cur_idx)
            cur = cur.next
            cur_idx += 1
        return indices

    @_no_cycle
    def pop(self) -> int:
        """Delete tail node and return its value"""
        if self.is_empty():
            raise IndexError("Cannot pop from empty LinkedList")
        prev = self._prehead
        for _ in range(self._length - 1):
            prev = prev.next
        popped = prev.next.val
        prev.next = None
        self._tail = prev
        self._length -= 1
        return popped

    def pop_left(self) -> int:
        """Delete head node and return its value"""
        if self.is_empty():
            raise IndexError("Cannot pop from empty LinkedList")
        prev = self._prehead
        popped = prev.next.val
        prev.next = prev.next.next
        self._length -= 1
        return popped

    @_no_cycle
    def to_array(self) -> list:
        """Return a traditional list representation of self"""
        out = []
        cur = self.get_head()
        while cur:
            out.append(cur.val)
            cur = cur.next
        return out

    def push(self, value: int) -> None:
        """Push a new node to end of list"""
        new_node = ListNode(value)
        prev = self._prehead if self.is_empty() else self.get_tail()
        prev.next = new_node
        self._tail = new_node
        self._length += 1

    def push_left(self, value: int) -> None:
        """Push a new node to front of list"""
        new_node = ListNode(value)
        prev = self._prehead
        if self.is_empty():
            new_node.next = None
            self._tail = new_node
        else:
            new_node.next = prev.next
        prev.next = new_node
        self._length += 1

    @_no_cycle
    def show(self) -> None:
        """Print items of self as a traditional list"""
        print(self.to_array())

    @_no_cycle
    def delete(self, target: int) -> None:
        """Delete first occurence of target value from self"""
        prev = self._prehead
        cur = prev.next
        while cur:
            if cur.val == target:
                prev.next = cur.next
                self._length -= 1
                if self._tail == cur:
                    self._tail = prev if prev != self._prehead else None
                return
            prev = cur
            cur = cur.next
        raise ValueError("Target value not found")

    @_no_cycle
    def delete_index(self, index: int) -> None:
        """Delete node at index from self"""
        if index < 0 or index > self._length - 1:
            raise IndexError
        prev = self._prehead
        cur = prev.next
        for _ in range(index):
            prev = prev.next
            cur = cur.next
        prev.next = cur.next
        self._length -= 1
        if self._tail == cur:
            self._tail = prev if index > 0 else None

    @_no_cycle
    def copy(self) -> LinkedList:
        """Return a copy of self"""
        out = LinkedList()
        cur = self._prehead
        copy = out._prehead
        while cur.next:
            copy.next = ListNode(cur.next.val)
            if self._tail == cur.next:
                out._tail = copy.next
            out._length += 1
            cur = cur.next
            copy = copy.next
        return out

    def has_cycle(self) -> bool:
        """Check if self has a cycle, using Floyd's cycle-finding algorithm"""
        slow = self.get_head()
        fast = slow
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if id(fast) == id(slow):
                return True
        return False

    @_no_cycle
    def reverse(self) -> None:
        """Reverse elements of self"""
        if self._length < 2:
            return
        cur = self.get_head()
        self._prehead.next = self._tail
        self._tail = cur
        prev = None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

    @_no_cycle
    def sort(self, reverse: bool = False) -> None:
        """Sort list nodes by value, using mergesort algorithm"""
        if self._length < 2:
            return

        def get_mid(head):
            slow = head
            fast = head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        def merge(A, B):
            prehead = ListNode()
            C = prehead
            while A and B:
                C.next = ListNode()
                C = C.next
                if not reverse and A.val < B.val or reverse and A.val > B.val:
                    C.val = A.val
                    A = A.next
                else:
                    C.val = B.val
                    B = B.next
            while A:
                C.next = ListNode()
                C = C.next
                C.val = A.val
                A = A.next
            while B:
                C.next = ListNode()
                C = C.next
                C.val = B.val
                B = B.next
            return prehead.next

        def recurse(head):
            if head is None or head.next is None:
                return head
            mid = get_mid(head)
            part2 = mid.next
            mid.next = None
            return merge(recurse(head), recurse(part2))

        cur = recurse(self.get_head())
        self._prehead.next = cur
        for _ in range(self._length - 1):
            cur = cur.next
        self._tail = cur

    @_no_cycle
    def sorted(self, reverse: bool = False) -> LinkedList:
        """Return a copy of list with nodes sorted by value"""
        copy = self.copy()
        copy.sort(reverse=reverse)
        return copy
