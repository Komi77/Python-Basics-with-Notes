def square(n):
    '''Takes out the square of any number'''
    print(n **2)

square(3)
square(7)
square(8)

print(square.__doc__)

#The the thing which is enclosed b/w 3 single quotes is known is a doc string, it is like a comment, but unlike a comment we can print it, by writting the variable name then .__doc__ 
#And the doc string can just be written below the function heading.


#EASTER EGG IN PYTHON:


#PEP 8:
#Zen in Python:
#Zen in pyhton is a poem that is accessed by writing 'import this'

import this
