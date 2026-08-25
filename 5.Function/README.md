# Function
 - Function is a piece of source code, separate from larger program, that performs a specific
   task. Such as specific work may need to use it in the program and in another one as well.

## Reason to use functions:
 - To reduce complex tasks into simple tasks
 - Eliminate duplicate codes (not repeate again)
 - We can used in another program.
 - Distribute tasks to multiple programmers (Divided the work between multiple users)
 - Hode implementation details - abstraction (Saperate simple task with complex to show
    more advance) improve the quality of programmer.
 - Improves debugging by improving traceability program (It makes easy to following debugging program manualy or using a debugging tool)


## What is Recursive function 
### Recursive function is a function defined inside itself via self-referential expression
    - The function continue running call itself and repeat its behaivor until some condition is met to return result
    - All recursive functions share a common structure made up of:
        - Recursive case: 
            . Decompose original problem into simpler instrances of the same problem
        - Base case:
            . Smallest instance of the same problem


# Definition of function 

def nameof_function(var):
    return the_job_of_function_body

# Recursive function means the function call itself at the end also used as factorial.