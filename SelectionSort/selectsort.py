#title           : selectsort.py
#description     : Sorting a set of numbers stored inside an array using selection sort algorithm.
#author          : Ramadhi Irawan
#date            : 2014-10-07
#version         : 0.2
#usage           : python selectsort.py
#notes           : Information about selection sort: http://en.wikipedia.org/wiki/Selection_sort
#python_version  : 2.7.x


class Selectsort:
    'Sorting an array implementing Selection sort algorithm'

    def __init__(self, array):
        self.array = array

    def sort(self):
        length = len(self.array)
        for x in range(length):
            minimum = min(self.array[x:])
            minIndex = self.array[x:].index(minimum)
            self.array[x + minIndex] = self.array[x]
            self.array[x] = minimum
        return self.array


my_array = [56, 61, 62, 732, 236, 2723, 42, 41, 212, 156, 552, 3412, 236, 66, 125]
my_result = Selectsort(my_array)
print my_result.sort()