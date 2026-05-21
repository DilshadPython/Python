# Data Structure Types
- standard > one-dimensional arry
- binary search tree can guarantee O(logN) running times
- associative-array stores key-value pairs and can guarantee 0(1) running times

To find the shortest path in a G(V,E) graph with Dijkstra's algorithm.
    - Without a proper data structure we find the shortest path in O(N^2) running time
    - with priority queues (heaps) we can reduce this running time to O(NIogN)

- Let's assume we want to find the spanning tree in a G(V,E) graph with Kruskal's algorithm
- Without a proper data structure we can find the spanning tree in O(E logV) running time
- with priority queues (heaps) we can reduce this running time to O(E+logV)

There is always a trade-off between memory usage and running time of the underlying algorithm.

# Abstract Data Types (ADTs)
- abstract data types define the model (logical description) for a certain data structure.
- it is like supertype in programming (interface or abstract classes)
- ADTs define the basic behavior - do not specify the implementation or the programming language etc.

# Examples:
abstract data types define the behavior without the implementation

STACK - push() and pop()
QUEUE - enqueue() and dequeue()

data structures are the concrete representations and implementations of the underlying data
we want to reduce the running time of operations to 0(1)!!
FOR example: arrays, linked lists etc ..

ABSTRACT DATA TYPE

| STACKS |
|--------|

DATA STRUCTURES


Data Structures and Abstract Data Types Quiz
1. Why is it good to use data structures?
- They make the given applications way more easier to implement
- They can reduce the running time of applications (Such as for Dijkstra's) CORRECT
    EXPLAIN BETTER
    (Using data structures effectively can optimize algorithms, like Dijkstra's algorithm, by improving 
    their efficiency, which ultimately leads to reduced running times for applications. This means that 
    the right data structures help to process data faster and enhance overall performance.)
- They make applications use less memory

2. What is the difference between data structures and abstract data types?
- No difference at all
- Data structures are the specifications and abstract data types are the concrete implementations
- Abstract data types are the specifications and data structures are the concrete implementations (CORRECT)
  (Abstract data types (ADTs) define a model for data that specifies the operations and behaviors without d
   etailing how they are implemented, while data structures are the actual implementations that store and
   manage this data. Understanding this distinction helps you grasp how algorithms utilize different data
   representations to achieve efficiency.)