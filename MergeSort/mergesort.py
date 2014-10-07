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

    def mergesort(self, array):
        result = []

        if len(array) < 2:
            return array

        mid = int(len(array) / 2)
        upper = self.mergesort(array[:mid])
        lower = self.mergesort(array[mid:])

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

my_array = [72, 152, 16, 954, 4, 2143, 374, 23, 56, 7, 96, 7, 69, 35, 67, 296]
my_data = Mergesort('Meh')
print my_data.mergesort(my_array)