import time

class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data, new_node):
        self.size += 1
        new_node.next_node = self.head
        self.new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node


if __name__ == "__main__":
    linked_list = LinkedList()

    now = time.time()

    for i in range(100000):
        linked_list.append(0, i)

    print('Appending time into linked list is %ss' % str(time.time() - now))

    array = []
    now = time.time()

    for i in range(100000):
        array.append(0, i)

    print('Appending time into Array is %ss' % str(time.time() - now))
