def selectionsort(data):
    length = len(data)
    for x in range(length):
        minimum = min(data[x:])
        minIndex = data[x:].index(minimum)
        data[x + minIndex] = data[x]
        data[x] = minimum
    return data

blah = [12,512,62,234,236,2723,42,1,2,51,62,3412,236]
print selectionsort(blah)