# Retrieving n-th Fibonacci Number
# Using Dynamic Programming

def dynamicFib(n):
    fibList = [0, 1, 1]
    for i in range(n-1):
        fibList[2] = fibList[1] + fibList[0]
        fibList[0] = fibList[1]
        fibList[1] = fibList[2]
    return fibList[2]

print dynamicFib(2)