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

    def qsort(self, array):
        if array:
            less, equal, greater = self.partition(array)
            return self.qsort(less) + equal + self.qsort(greater)
        return array

my_array = [12, 434, 515, 26, 7, 3, 122, 15, 100, 152, 167, 623, 724, 541, 523, 1, 4, 3, 50, 79]
my_result = Quicksort("Quicksort")
print my_result.qsort(my_array)
