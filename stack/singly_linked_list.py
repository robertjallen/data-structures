class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node
    def get_value(self):
        return self.value
    def get_next(self):
        return self.next_node
    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next
class LinkedList:
    def __init__(self):
        self.head: Node = None  # points to the first node in the list
        self.tail: Node = None  # Points to the last node in the list
        self.length = 0
    def __str__(self):
        pass
    def add_to_head(self, value):
        new_node = Node(value)
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.set_next(self.head)
            self.head = new_node
    def add_to_tail(self, value):
        # Check if there's a tail
        # If there is no tail (empty list)
        if self.tail is None:
            # Create a new node
            new_tail = Node(value, None)
            #    Set self.head and self.tail to the new node
            self.head = new_tail
            self.tail = new_tail
        # If there is a tail (general case):
        else:
            # Create a new node with the value we want to add, next = None
            new_tail = Node(value, None)
            # Set current tail.next to the new node
            old_tail = self.tail
            old_tail.next_node = new_tail
            # Set self.tail to the new node
            self.tail = new_tail
        self.length += 1
    def remove_head(self):
        # If not head (empty list)
        if self.head is None:  # if self.head is None
            return None
        # List with one element:
        if self.head == self.tail:
            # Set self.head to current_head.next / None
            current_head = self.head
            self.head = None
            # Set self.tail to None
            self.tail = None
            # Decrement length by 1
            self.length = self.length - 1
            return current_head.value
        # If head (General case):
        else:
            # 	Set self.head to current_head.next
            current_head = self.head
            self.head = current_head.next_node
            #  Return current_head.value
            self.length = self.length - 1
            return current_head.value
    def remove_tail(self):
        # first if you donnt have head (aka no linked list exists),
        if not self.head:
            return None
        # if linked list has 1 node
        if self.head is self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            return value
        current = self.head
        while current.get_next() is not self.tail:
            current = current.get_next()  # goes through entire list until next node is tail
        # save value of tail beause that is what we will return later
        value = self.tail.get_value()
        self.tail = current  # now tail is also current
        self.tail.set_next(None)
        return value