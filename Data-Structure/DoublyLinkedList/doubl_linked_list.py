
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    # Add the item to the end of linked list, we have to manipulate the tail node in 0(1) running time
    def append(self, data):
        new_node = Node(data)

        # The list is Empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # here is when the list not empty or had at least one item
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    # traverser forward
    def traverse_front(self):
        current_node = self.head

        while current_node is not None:
            print('%d', current_node.data)
            current_node = current_node.next

    # traverser backword
    def traverse_back(self):
        current_node = self.tail

        while current_node is not None:
            print('%d', current_node.data)
            current_node = current_node.prev

if __name__ == '__main__':
    linked_list = DoublyLinkedList()

    # item = input('Enter item: ')
    linked_list.append(2)
    linked_list.append(4)
    linked_list.append(6)

    # outout must be 1 2 3
    linked_list.traverse_front()
    print('============')
    # output must be 3 2 1
    linked_list.traverse_back()