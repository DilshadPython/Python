- Serialization means persistent storage, i.e., todisk
- Relational storage writes data to tables (Relational db text files)
- Object-based storage stores objects as they are used in code
- Object dbes
- Object-relational mappings can mediate between the two

# Pickle and cPickle
- Python-native object storage
- Can store most Python objects on disk
- Does not store classes, modules or function, but can refer to them
- Not readable for human
- Uses the pickle protocol which changes between versions of Python
- cPickle is a faster, C-compiles implementation
 
# What is Python Pickle

- Its serialize and de-serialize python module from byte-stream to binary-byte 
- and back again 