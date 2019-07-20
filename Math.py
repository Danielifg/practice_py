import math
import matplotlib.pyplot as plt  
import numpy as np

i = math.log2(50)
print(math.log2(50))
# exponential = ^
print(2**i)

# factorial
def fact(n):
    if n == 0:
        return 1;
    return n * fact(n-1)

print(fact(5))


x = [2, 4, 6, 8, 10, 12]
dic = {
    'a':'b',
    'c':'d','c':'d','c':'d','dddd':'ddd','c':'d'
}
print('ddd' in dic.values())

# Constant Complexity 
#y = [2, 2, 2, 2, 2, 2]

# Linear Complexity ( incremental )
y = [2, 4, 6, 8, 10, 1]

plt.plot(x, y, 'b')  
plt.xlabel('Inputs')  
plt.ylabel('Steps')  
plt.title('Constant Complexity')  
#plt.show()  