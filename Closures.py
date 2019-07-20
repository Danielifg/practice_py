
"""
 Closure Example
 This technique by which some data ("Hello") 
 gets attached to the code is called closure.
"""
def printer0(msg):
    def printer():
        print(msg)
    return printer
another = printer0("Hello") # closure
another()

# Closure ex:2
def outter(n):
    def mult(x):
        return n * x
    return mult
closure = outter(3)
print(closure(5))
# all closure Objects have
# __closure__ attribute @return tuple 
# of cell objects
print(closure.__closure__[0].cell_contents)

