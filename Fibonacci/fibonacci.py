#title           : fibonacci.py
#description     : Get fibonacci number between 0 - 10,000,000
#author          : Ramadhi Irawan
#date            : 2014-10-07
#version         : 0.2
#usage           : python fibonacci.py
#notes           : Information about fibonacci number: http://en.wikipedia.org/wiki/Fibonacci_number
#python_version  : 2.7.x

class Fibonacci:
    'Sorting an array implementing Fibonacci algorithm'

    def __init__(self, mode):
        self.mode = mode

    def isPrime(self, number):
        n = abs(int(number))
        if n < 2:
            return False

        if n == 2:
            return True

        if not n & 1:
            return False

        for x in range(3, int(n**0.5)+1, 2):
            if n % x == 0:
                return False
        return True

    def getFibonacci(self):
        list = []
        a, b = 0, 1
        while b < 10000000:
            if self.mode == 1:
                if self.isPrime(b):
                    list.append(b)
            elif self.mode == 0:
                list.append(b)
            a, b = b, a+b
        return list

normalFib = Fibonacci(0)
primeFib = Fibonacci(1)

result_normal = normalFib.getFibonacci()
result_prime = primeFib.getFibonacci()

print "Fibonacci numbers between 0 - 10,000,000:"
print result_normal
print "Average is: ", reduce(lambda x, y: x+y, result_normal) / len(result_normal), "(rounded to nearest integer)"
print
print "Prime Fibonacci numbers between 0 - 10,000,000:"
print result_prime
print "Average is: ", reduce(lambda x, y: x+y, result_prime) / len(result_prime), "(rounded to nearest integer)"