#title           : insertsort.py
#description     : Sorting a set of numbers stored inside an array using insertion sort algorithm.
#author          : Ramadhi Irawan
#date            : 2014-10-07
#version         : 0.2
#usage           : python insertsort.py
#notes           : Information about bubble sort: http://en.wikipedia.org/wiki/Insertion_sort
#python_version  : 2.7.x

__author__ = 'Ramadhi Irawan'


class InsertionSort:
    'Sorting an array implementing Insertion Sort algorithm'

    def __init__(self, array):
        self.array = array

    def sort(self):
        first = 0
        last = len(self.array) - 1
        nextpos = last - 1
        while nextpos >= first:
            next = self.array[nextpos]
            current = nextpos
            while (current < last) and (self.array[current] > self.array[current + 1]):
                current = current + 1
                self.array[current - 1], self.array[current] = self.array[current], self.array[current - 1]
            self.array[current] = next
            nextpos = nextpos - 1
        return self.array

import random
my_array = random.sample(range(100), 21)
print "Your array before sorting: ", my_array
my_result = InsertionSort(my_array)
print "You array after sorting: ", my_result.sort()