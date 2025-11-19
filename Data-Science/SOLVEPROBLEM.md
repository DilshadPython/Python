Pseudocode

PROGRAM make a Tea

WHILE (water not boiled):
    boil water
ENDWHILE

put water in cup

WHILE(sugar need):
    add sugar
ENDWHILE

WHILE(milk need):
    add milk
ENDWHILE

WHILE(need to stir):
    sire Tea again
ENDWHILE

Serve it and Finish

#################################################

Next step:
'''
This is only to explain:
L = [12, 1, -9, 44, -5, 22, 69]

n is a number of the length of list which is 6
counter(2) take the second index of the list which is -4

'''


-   Search Minimum:

searchminFormList(L,n):

    minValue = L[1]
    counter = 2
    While (counter <= n):
        v = L[counter]
        if(v<minValue>):
            minValue = v      (counter += 1)
        else:
            pass  
        endif
    endwhile

    return minValue

endSearchMinFromList