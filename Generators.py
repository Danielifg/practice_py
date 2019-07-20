"""
Generator function contains one or more yield statement.
When called, it returns an object (iterator) 
but does not start execution immediately.
Methods like __iter__() and __next__() are 
implemented automatically. So we can iterate
through the items using next().
Once the function yields, the function is 
paused and the control is transferred to the
caller.Local variables and their states are 
remembered between successive calls.
Finally, when the function terminates, 
StopIteration is raised automatically on 
further calls.
"""

# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n

a = my_gen()
next(a)




# reverse String
def getLength(string):
    length = len(string)
    for i in range(length -1,-1,-1):
        yield string[i]

for char in  getLength("xanipupu"):
    print()

