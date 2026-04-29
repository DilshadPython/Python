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

    # This is 0(1) constant running time
    def insert_start(self, data):
        self.num_of_nodes += 1
        new_node = Node(data)

        # if the head is NULL (so the data structure is empty)
        if self.head is None:
            self.head = new_node
        # else when linked list is not empty at least has one data
        else:
            # Here update the references
            new_node.next_node = self.head
            self.head = new_node

    # insert or add data at the end
    def insert_end(self, data):
        self.num_of_nodes += 1
        new_node = Node(data)

        # check if linked list empty
        if self.head is None:
            self.head = new_node
        else:
            # Here else which is mean linked list is not empty
            actual_node = self.head

            # Here it has 0(N) linear running time
            while actual_node.next_node is not None:
                actual_node = actual_node.next_node

            # The actual_node is the last node: so we insert the new_node right after the actual_node
            actual_node.next_node = new_node

    # constant running time 0(1)
    def size_of_list(self):
        return self.num_of_nodes

    # 0(N) linear running time
    def traverse(self):
        actual_node = self.head

        while actual_node is not None:
            print(actual_node)
            actual_node = actual_node.next_node

if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert_start(input("Enter data to the beginning of the linked list: "))
    linked_list.insert_start(input("Enter data to the beginning of the linked list: "))
    linked_list.insert_end(input("Enter data to the beginning of the linked list: "))
    linked_list.traverse()
    print("Size of list now: ", linked_list.size_of_list())
    linked_list.insert_end(input("Enter data to the end of list: "))
    linked_list.traverse()
