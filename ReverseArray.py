
arr = [1,4,2,3]
#arr.reverse()
#print(arr)

pow2 = [2 ** x for x in range(10)]
#print(pow2)

def fibonacci(n):
    if n <= 0: return 0
    elif n == 1 : return 1
    return(fibonacci(n-1) + fibonacci(n-2))

#print(fibonacci(30))

start = 1
end = 15
def sort(start,end):
    arr = []
    for i in range(start,end):
        if i%2!=0:
            arr.append(i)
    return arr

print(sort(start,end))