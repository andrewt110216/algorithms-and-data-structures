import queue
from collections import deque

# Note the following properties of binary trees when represented as lists
# Let i represent the counting position, starting from 1 (i.e. index + 1),
# and n represent the length of the list:
# 1. Parent Node
#      a. if i == 1, then node i has no parent node (it is the root)
#      b. if i > 1, then the parent node of i is node (i // 2)
# 2. Left Child Node
#      a. if 2i > n, then node i has no left child
#      b. if 2i <= n, then the left child of node i is node 2i
# 3. Right Child Node
#      a. if 2i + 1 > n, then node i has no right child
#      b. if 2i + 1 <= n, then the right child of node i is node 2i + 1
# 4. Left Sibling
#      a. if i > 1 is odd, then the left sibling of node i is node i - 1
# 5. Right Sibling
#      a. if i < n is even, then the right sibling of node i is node i + 1
# 6. Level of a Node
#      a. the root node is level 1
#      b. the level of node i = floor( log2(i) ) + 1


class TreeNode:
    """Represent the node of a binary tree"""

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def print(self):
        def recurse(self, space):
            if self is None:
                return
            space += 10
            recurse(self.right, space)
            print()
            for _ in range(10, space):
                print(end=" ")
            print(self.val)
            recurse(self.left, space)

        recurse(self, 0)
        return

    def __repr__(self):
        return f"<TreeNode {str(tree_to_array(self))}>"

    def __eq__(self, root2):
        """Compare two binary trees"""

        # check for empty input
        if not self and not root2:
            return True
        if not self or not root2:
            return False

        # use level-order traversal on both trees and compare each node
        q1 = deque([self])
        q2 = deque([root2])
        while q1 and q2:
            cur1 = q1.popleft()
            cur2 = q2.popleft()
            if cur1 and cur2:
                if cur1.val != cur2.val:
                    return False
                q1.append(cur1.left)
                q1.append(cur1.right)
                q2.append(cur2.left)
                q2.append(cur2.right)

            # if only one of cur1 and cur2 are not None, the trees do not match
            elif cur1 or cur2:
                return False

        # if either q is not empty, the trees do not match
        if q1 or q2:
            return False
        return True


def array_to_tree(array: list) -> TreeNode:
    """Convert a list to a TreeNode object (binary tree)"""
    if len(array) == 0:
        return None

    def recurse(i=0):
        if i > len(array) - 1 or array[i] is None:
            return None
        node = TreeNode(array[i])
        node.left = recurse(2 * i + 1)
        node.right = recurse(2 * i + 2)
        return node

    return recurse()


def tree_to_array(root: TreeNode) -> list:
    """Convert a binary tree (given the root node) to a list"""
    array = []
    if root:
        q = queue.Queue()
        q.put(root)
        while not q.empty():
            cur = q.get()
            if cur:
                array.append(cur.val)
                q.put(cur.left)
                q.put(cur.right)
            else:
                array.append(None)
    # Clean up trailing None's
    while array[-1] is None:
        array.pop()
    return array


if __name__ == "__main__":

    # Display a few demonstrations of the TreeNode class and related functions
    print()
    print(" Demonstrations of TreeNode and Related Functions ".center(78, "="))
    print()

    # Demonstrate how to create a binary tree from the TreeNode class
    print(" Create a binary tree from TreeNodes ".center(78, "-"))
    print()

    #      1
    #    /   \
    #   2     3
    #  / \   / \
    # 4   5 6   7

    # create nodes
    root = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)

    # connect them
    root.left = node2
    root.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7

    # print the head node to see the entire linked list
    print("> My binary tree:", root)
    assert root.__repr__() == "<TreeNode [1, 2, 3, 4, 5, 6, 7]>"
    print("\n> Visual representation of my binary tree:")
    root.print()
    print()

    # Demonstrate how to convert a binary tree to a traditional list
    print(" Convert a binary tree to a traditional list ".center(78, "-"))
    print()

    my_list = tree_to_array(root)
    print("> My binary tree converted to a traditional list:", my_list)
    assert my_list == [1, 2, 3, 4, 5, 6, 7]
    print()

    # Demonstrate how to convert traditional list to a binary tree
    print(" Convert a traditional list to a binary tree ".center(78, "-"))
    print()

    my_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print("> My traditonal list is:", my_list)
    my_binary_tree = array_to_tree(my_list)
    print("> My traditional list converted to a binary tree:", my_binary_tree)
    print("\n> Visual representation of my binary tree:")
    my_binary_tree.print()
    print()

    # Demonstrate comparison of tree nodes
    print(" Compare two TreeNodes ".center(78, "-"))
    print()

    binary_tree_1 = array_to_tree([1, 2])
    binary_tree_2 = array_to_tree([1, 2, 3])
    print("> binary_tree_1:", binary_tree_1)
    print("> binary_tree_2:", binary_tree_2)
    print("> Run Comparison: `binary_tree_1 == binary_tree_2`")
    print("  > Return:", binary_tree_1 == binary_tree_2)
    assert binary_tree_1 != binary_tree_2
    print()

    binary_tree_1 = array_to_tree([1, 2, 3])
    binary_tree_2 = array_to_tree([1, 2, 3])
    print("> binary_tree_1:", binary_tree_1)
    print("> binary_tree_2:", binary_tree_2)
    print("> Run Comparison: `binary_tree_1 == binary_tree_2`")
    print("  > Return:", binary_tree_1 == binary_tree_2)
    assert binary_tree_1 == binary_tree_2
    print()

    binary_tree_1 = array_to_tree([])
    binary_tree_2 = array_to_tree([None])
    print("> binary_tree_1:", binary_tree_1)
    print("> binary_tree_2:", binary_tree_2)
    print("> Run Comparison: `binary_tree_1 == binary_tree_2`")
    print("  > Return:", binary_tree_1 == binary_tree_2)
    assert binary_tree_1 == binary_tree_2
    print()

    print("".center(78, "="))
    print()
