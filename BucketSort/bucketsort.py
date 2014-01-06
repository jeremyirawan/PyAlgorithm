def bucketsort(data):
    arr = []
    count = [0] * len(data)
    
    for x in data:
        count[x] += 1
    
    for y, amount in enumerate(count):
        data.extend([y] * amount)
    
    return arr

blah = [24,125,67,8,35,45,23,856,4,347,56,34,65,234,45]
print bucketsort(blah)