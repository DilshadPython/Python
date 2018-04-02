### Sort

#### Help on method_descriptor:

sort(...)
    L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*
    	   key = sorting function


### reverse = False ==> Sort in ascending order
### reverse = True ==> Sort in descending order

#### 'in-place' Algorithm 
##### Does not create a secomd data structure
##### Modifies input/existing structure

### list.sort() changed the list
### Q: can we create a sorted copy?
### Q: how we sort a tuple
### A: for all above we use sorted() method