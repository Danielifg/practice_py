"""
Algorithm runtimes examples

    Key to understanding Big O is
    understanding the rates at which 
    things can grow.
"""
 
 # O(n) linear complexity
def linear_algo(items):  
    for item in items:
        print(item)

    for item in items:
        print(item)

linear_algo([4, 5, 6, 8])  

# O(1)
def constant_algo(items):  
    result = items[0] * items[0]
    print ()

# O(n**2) Quadratic Complexity 
# normally nested for loops
def quadratic_algo(items):  
    for item in items:
        for item2 in items:
            print(item, ' ' ,item)

