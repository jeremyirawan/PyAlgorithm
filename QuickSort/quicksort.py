#title           : quicksort.py
#description     : Sorting a set of numbers stored inside an array using quick sort algorithm.
#author          : Ramadhi Irawan
#date            : 2014-10-07
#version         : 0.2
#usage           : python quicksort.py
#notes           : Information about merge sort: http://en.wikipedia.org/wiki/Quicksort
#python_version  : 2.7.x

class Quicksort:
    'Sorting an array implementing Quicksort algorithm'

    def __init__(self, name):
        self.name = name

    def partition(self, array):
        pivot = array[0]
        less, equal, greater = [], [], []
        for x in array:
            if x < pivot:
                less.append(x)
            elif x > pivot:
                greater.append(x)
            else:
                equal.append(x)
        return less, equal, greater

    def sort(self, array):
        if array:
            less, equal, greater = self.partition(array)
            return self.sort(less) + equal + self.sort(greater)
        return array


import random
my_array = random.sample(range(361), 37)
print "Your array before sorting: ", my_array
my_result = Quicksort("Quick Sort")
print "You array after sorting: ", my_result.sort(my_array)
