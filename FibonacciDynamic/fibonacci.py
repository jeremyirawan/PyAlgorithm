#title           : fibonacci.py
#description     : Get n-th fibonacci number using dynamic programming
#author          : Ramadhi Irawan
#date            : 2014-10-07
#version         : 0.2
#usage           : python fibonacci.py
#notes           : Information about fibonacci number: http://en.wikipedia.org/wiki/Fibonacci_number
#                  Information about dynamic programming: http://en.wikipedia.org/wiki/Dynamic_programming
#python_version  : 2.7.x

class Fibonacci:
    'Sorting an array implementing Fibonacci algorithm'

    def __init__(self, number):
        self.number = number

    def getFibonacci(self):
        catalyst = [0, 1, 1]
        for i in range(self.number - 1):
            catalyst[2] = catalyst[1] + catalyst[0]
            catalyst[0] = catalyst[1]
            catalyst[1] = catalyst[2]
        return catalyst[2]

sequence = 10
number = Fibonacci(sequence)
print "The ", sequence, "-th fibonacci number is: ", number.getFibonacci()