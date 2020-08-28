"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

from collections import deque
from stack import Stack


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left: BSTNode = None  # Either a BSTNode or None
        self.right: BSTNode = None

    # Insert the given value into the tree
    def insert(self, value):
        # Compare target value to node.value
        # If value > node.value:
        if value >= self.value:
            # Go right
            # If node.right is None:
            if self.right is None:
                # Create the new node there
                self.right = BSTNode(value)
            else:  # self.right is a BSTNode
                # Do the same thing (aka recurse)
                # Insert value into node.right
                # right_child is a BSTNode, so we can call insert on it
                right_child = self.right
                right_child.insert(value)
        # Else if value < node.value
        if value < self.value:
            # Go Left
            # If node.left is None:
            if self.left is None:
                # Create node
                self.left = BSTNode(value)
            else:
                # Do the same thing
                # (compare, go left or right)
                # Insert value into node.left
                left_child = self.left
                left_child.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Contains:
        # Compare target value to node.value
        if target == self.value:
            return True
        if target >= self.value:
            if self.right:
                return self.right.contains(target)
        # Go right
        # If node.right is None:
        # We've traversed the tree and haven't found it
        # return False
        # Else:
        # Do the same thing
        # return node.right.contains(target)
        # Else if target < node.value
        if target < self.value:
            if self.left:
                return self.left.contains(target)
        # Go Left
        # If node.left is None:
        # return False
        # Else:
        # Do the same thing
        # (compare, go left or right)
        # return node.left.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        current_node = self
        while current_node.right is not None:
            current_node = current_node.right
        return current_node.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # Will have to look at both branches
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self.left:
            self.left.in_order_print(node)
        print(self.value)
        if self.right:
            self.right.in_order_print(node)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
        queue = deque()
        queue.append(node)

        while len(queue) > 0:

            cur_node = queue.popleft()
            

            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)
            print(cur_node.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node):

        stack = Stack()
        current_node = stack.push(node)
        
        while stack.size > 0:
            current_node = stack.pop()

            if current_node.left:
                stack.push(current_node.left)
            if current_node.right:
                stack.push(current_node.right)
            print(current_node.value)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    # def pre_order_dft(self):
    #     pass

    # # Print Post-order recursive DFT
    # def post_order_dft(self):
    #     pass


"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print(bst)
bst.dft_print(bst)

print("elegant methods")
print("pre order")
# bst.pre_order_dft()
print("in order")
# bst.in_order_dft()
print("post order")
# bst.post_order_dft()