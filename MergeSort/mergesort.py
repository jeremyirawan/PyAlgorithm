#title           : mergesort.py
#description     : Sorting a set of numbers stored inside an array using merge sort algorithm.
#author          : Ramadhi Irawan
#date            : 2014-10-07
#version         : 0.2
#usage           : python mergesort.py
#notes           : Information about merge sort: http://en.wikipedia.org/wiki/Merge_sort
#python_version  : 2.7.x

class Mergesort:
    'Sorting an array implementing Fibonacci algorithm'

    def __init__(self, name):
        self.name = name

    def sort(self, array):
        result = []

        if len(array) < 2:
            return array

        mid = int(len(array) / 2)
        upper = self.sort(array[:mid])
        lower = self.sort(array[mid:])

        while (len(upper) > 0) or (len(lower) > 0):
            if len(upper) > 0 and len(lower) > 0:
                if upper[0] > lower[0]:
                    result.append(lower[0])
                    lower.pop(0)
                else:
                    result.append(upper[0])
                    upper.pop(0)
            elif len(lower) > 0:
                for i in lower:
                    result.append(i)
                    lower.pop(0)
            else:
                for i in upper:
                    result.append(i)
                    upper.pop(0)
        return result

import random
my_array = random.sample(range(512), 45)
print "Your array before sorting: ", my_array
my_result = Mergesort("Merge Sort")
print "You array after sorting: ", my_result.sort(my_array)