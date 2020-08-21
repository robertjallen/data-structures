"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next


"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):
        if self.length == 0:
            newNode = ListNode(value)
            newNode.prev == None
            newNode.next == None
            newNode.value == value
            self.head = newNode
            self.tail = newNode
            self.length += 1
        else:
            newNode == ListNode(value)
            self.head.prev = newNode
            newNode.next = self.head
            newNode.prev = None
            newNode.value = value
            self.length += 1

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        if self.length == 0:
            return None
        if self.length == 1:
            old_value = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return old_value
        else:
            old_value = self.head.value
            current_node = self.head.next
            current_node.prev = None
            self.head = current_node
            self.length -= 1
            return old_value

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        if self.length == 0:
            newNode = ListNode(value)
            newNode.next = None
            newNode.prev = None
            self.head = newNode
            self.tail = newNode
            self.length += 1
        else:
            newNode = ListNode(value)
            old_tail = self.tail
            old_tail.next = newNode
            newNode.prev = old_tail
            newNode.next = None
            self.length += 1

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        if self.length == 0:
            return None
        if self.length == 1:
            old_value = self.head.value
            self.tail = None
            self.head = None
            self.length -= 1
        else:
            old_value = self.tail.value
            old_tail = self.tail
            new_tail = self.tail.prev
            new_tail.next = None
            old_tail.prev = None
            self.tail = new_tail
            return old_value

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        pass

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        pass

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node):
        pass
        # Check for empty pointers
        # Get previous node = node.prev
        # Set prev_node.next to node.next
        # Next_node = node.next
        # Set next_node.previous = previous_node
        # Decrement length
        # Set node.prev = None
        # Set node.next = None
        # Return node.value

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):
        # If length == 0 return None
        if self.length == 0:
            return None
        # If length == 1 return self.head.value
        if self.length == 1:
            return self.head.value
        # Current_max starts out as self.head.value
        current_max = self.head.value
        # Iterate through the list
        current_node = self.head
        # Stop when current_node is None
        while current_node is not None:
            # Compare current_max to each value and update current_max if value > current_max
            if current_max < current_node.value:
                current_max = current_node.value
            # Move current_node forward
            current_node = current_node.next
        # Return current_max
        return current_max