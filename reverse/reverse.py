class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        # wrap value in a node
        node = Node(value)
        # if head is not empty then set 'set_next' to the old head
        if self.head is not None:
            node.set_next(self.head)
        # set the head to the new node    
        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # initiate new_head variable to hold new head value
        new_head = None
        # while we are iterating through nodes
        while node:
            # hold the next node's value in a temporary variable
            tmp = node.next_node
            # assign the node's next_node to the new_head value
            node.next_node = new_head
            # assign the new_head value to be that of the node
            new_head = node
            # assign the node's new value to be that of the old next and then repeat
            node = tmp
        # assign the head to be the new head
        self.head = new_head
        # return the new_head
        return new_head