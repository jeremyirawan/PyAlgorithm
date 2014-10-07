#title           : bucketsort.py
#description     : Sorting a set of numbers stored inside an array using bucket sort algorithm.
#author          : Ramadhi Irawan
#date            : 2014-10-07
#version         : 0.2
#usage           : python bucketsort.py
#notes           : Information about bubble sort: http://en.wikipedia.org/wiki/Bucket_sort
#python_version  : 2.7.x

class Bucketsort:
    'Sorting an array implementing Bubblesort algorithm'

    def __init__(self, dataset):
        self.dataset = dataset

    def sort(self):
        max = self.dataset[0]
        for x in self.dataset:
            if x > max:
                max = x

        bucket = [0]*(max + 1)
        for y in self.dataset:
            bucket[y] += 1

        result = []
        for i in range(max+1):
            for j in range(bucket[i]):
                result.append(i)

        print result

import random
my_array = random.sample(range(250), 17)
print "Your array before sorting: ", my_array
my_result = Bucketsort(my_array)
print "You array after sorting: ", my_result.sort()