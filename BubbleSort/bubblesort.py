def bubblesort(data):
    length = len(data)-1
    sorted = False
    
    while not sorted:
        sorted = True
        for x in range(length):
            if(data[x]) > data[x+1]:
                sorted = False
                data[x],data[x+1] = data[x+1], data[x]
    return data

blah = [123,51,23,152,61,512,6,24,62,723,342,523,12,532,63,73]
print bubblesort(blah)