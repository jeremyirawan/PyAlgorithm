#title           : bubblesort.py
#description     : Sorting a set of numbers stored inside an array using bubble sort algorithm.
#author          : Ramadhi Irawan
#date            : 2014-10-07
#version         : 0.2
#usage           : python bubblesort.py
#notes           : Information about bubble sort: http://www.sorting-algorithms.com/bubble-sort
#python_version  : 2.7.x

class Bubblesort:
    'Sorting an array implementing Bubblesort algorithm'

    def __init__(self, dataset):
        self.dataset = dataset

    def sortBubble(self):
        length = len(self.dataset)-1
        sorted = False

        while not sorted:
            sorted = True
            for x in range(length):
                if(self.dataset[x]) > self.dataset[x+1]:
                    sorted = False
                    self.dataset[x], self.dataset[x+1] = self.dataset[x+1], self.dataset[x]
        print self.dataset

my_array = [123,51,23,152,61,512,6,24,62,723,342,523,12,532,63,73]
my_data = Bubblesort(my_array)
my_data.sortBubble()