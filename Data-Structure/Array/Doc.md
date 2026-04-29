Linked List

# Description of inserting to liked list from beginning 

func insertBeginning(List list, Node newNode):
    newNode.next := list.firstnode
    list.firstNode := newNode

# Inserting to the End of linkedlist:

node := list.firstNode
while node not null:
    (do something with node.data)
    node := node.next

newNode.next := node.next
node.next := newNode

# Remove first item from beginning linked list:

# Remove first item from end of linked list:

# Operation                             Running Time
find first item(head node)                  0(1)
search for arbitrary item                   0(N)
insert item to the beginning                0(1)
insert item to arbitrary position           0(N)
remove first item                           0(1)
removing arbitrary item                     0(N)

# Linked List
# Pros                                                              Cons
1. Dynamic Structures                                           1. More Memory
They can acquire memory at run time without resizing the        Linked lists need more memory than arrays because we 
data structure                                                  have to store the references    

2. Grow Data Structure Organically                              2. No Random Access
No problem if we do not know the number of items we want        There are no indexes  we can access the first node
to store at compile time                                        (head node) exclusively

3. Can Store Different Sized Items                              3. Can not go backwards
arrays on the other hand assume the items have the exact        how to access the previous item? 
same size
                                                                4. No Predictable
                                                                running time of the application depends on what 
                                                                operations the users do
