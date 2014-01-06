def isPrime(number):
    n = abs(int(number))
    if n < 2:
        return False;
    
    if n == 2:
        return True;
    
    if not n & 1:
        return False
    
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

# SELECT MODE:
# 1 - GET PRIME FIBONACCI
# 2 - GET FIBONACCI LIST
def getFibonacci(mode):
    list = []
    a,b = 0,1
    while b < 10000000:
        if mode == 1:
            if(isPrime(b) == True):
                list.append(b)
                #print b,
        elif mode == 0:
            list.append(b)
            #print b,
        a,b = b, a+b
    return list
        
normalFib = getFibonacci(0)
primeFb = getFibonacci(1)


print "Fibonacci numbers between 0 - 10,000,000:"
print normalFib
print "Average is: ", reduce(lambda x,y: x+y, normalFib) / len(normalFib), "(rounded to nearest integer)"
print
print "Prime Fibonacci numbers between 0 - 10,000,000:"
print primeFb
print "Average is: ", reduce(lambda x,y: x+y, primeFb) / len(primeFb), "(rounded to nearest integer)"