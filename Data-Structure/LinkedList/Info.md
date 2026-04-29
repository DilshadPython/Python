Revisiting remove operation
In the theoretical section we stated that remove operation is quite fast with linked lists. But during the 
implementation we saw that it has O(N) linear running time complexity - which is not that fast. Why?

The answer is that usually when we use linked lists - we assume that we have to remove (and insert) the first 
item which is the head node that can be accessed in O(1) constant running time.



the remove function we have implemented is totally fine

if we use it to remove arbitrary item then of course first we have to find it and then we have to update the 
references (exactly how we have implemented it) - with O(N) running time

if we want to remove the first node (head node) with the same function - then of course there is no need for
the while loop (Python will exit the while loop after the first iteration) so the final running time is O(1)

CONCLUSION: WE CAN REMOVE THE FIRST NODE OF THE LINKED LIST EXTREMELY FAST - WITH O(1) CONSTANT RUNNING TIME

This is exactly the reason why we have linked list data structure - to be able to manipulate the first item 
extremely fast.

# Arrays and Linked Lists
1. Dynamic and static data structures
   - Arrays are static data structures - we have to know the size of the data structures in advance
   (or we have to resize it)
   - Linked lusts are dynamic data structures - they can grow organically based on the references
   ( no resize operation needed)
2. Random access (Random Indexing)
   - items in an array are located right next to each other in the main memory(RAM) this is why we can use indexes
   - There is no random access in a Linked list data structures 
3. Manipulating the first items
   - We have to shift several items (all the items in worst-case) when manipulating the first items in arrays
   - Linked list are dynamic data structures - we just have to update the references around the head node
4. Manipulating the first items
   - There can not be holes in the data structure when manipulating the last items in arrays
   - Linked lists have access to the first node (head node) exclusively so in this case have to traverse the whole
   O(N) running time
5. Memory Management
   - Arrays do not need any extra memory
   - Linked lists on the other hand do need extra memory because of te references (pointers) each node linked to other

# Searching for an arbitrary item (or removing an arbitrary item) takes O(N) linear running time for 
# both data structures
                                                Linked Lists                              Arrays
 Search                                              O(N)                                  O(1)
 insert at the start                                 O(1)                                  O(N)
 insert at the end                                   O(N)                                  O(1)
 waste space                                         O(N)                                   O
 
