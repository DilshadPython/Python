class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

    def __repr__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        # The head node in the linkedlist call first node, that we can access this node exclusively
        self.head = None
        self.num_of_nodes = 0
