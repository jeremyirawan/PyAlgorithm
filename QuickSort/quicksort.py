def partition(data):
    pivot = data[0]
    less, equal, greater = [], [], []
    for x in data:
        if x < pivot:
            less.append(x)
        elif x > pivot:
            greater.append(x)
        else:
            equal.append(x)
    return less, equal, greater

def qsort(data):
    if data:
        less, equal, greater = partition(data)
        return qsort(less) + equal + qsort(greater)
    return data

blah = [12,4,5,6,7,3,1,15,100,152,167,623,724,541,523,1]
print qsort(blah) 
