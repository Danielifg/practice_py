"""
Transpose of a matrix is the interchanging of rows and columns. It is denoted 
as X'. The element at ith row and jth column in X will be placed at
jth row and ith column in X'. So if X is a 3x2 matrix, X' will be a 2x3 matrix.
"""

# Program to transpose a matrix using nested loop
X = [[12,7],[4 ,5],[3 ,8]]
result = [[0,0,0],[0,0,0]]
# iterate through rows  
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[j][i] = X[i][j]
for r in result:
   print(r)

''' Program to transpose a matrix using list comprehension'''
X = [[12,7],[4 ,5],[3 ,8]]
result = [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]
for r in result: print(r)

# Program to multiply two matrices using nested loops

# 3x3 matrix
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
# 3x4 matrix
Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]
# result is 3x4
result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

for i in range(len(X)):
       for j in range(len(Y[0])):
              for k in range(len(Y)):
                      result[i][j]  += X[i][k] * Y[k][j]
def func(result):
   for r in result:             
       yield print(r)

next(func(result))    
c=10
c|=3
print(c)


            
               
                  
               
