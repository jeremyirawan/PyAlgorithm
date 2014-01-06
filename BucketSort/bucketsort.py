def bucketSort(data):
    max = data[0]
    for x in data:
        if x > max:
            max = x
    
    bucket = [0]*(max + 1)
    for y in data:
        bucket[y] += 1
    
    result = []
    for i in range(max+1):
        for j in range(bucket[i]):
            result.append(i)
    return result

blah = [123,512,5,6,2,1,123,1,25,1,26]
print bucketSort(blah)