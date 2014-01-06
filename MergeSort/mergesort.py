def mergesort(data):
    result = []
    
    if len(data) < 2:
        return data
    
    mid = int(len(data) / 2)
    upper = mergesort(data[:mid])
    lower = mergesort(data[mid:])
    
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

blah = [32,152,16,23,25,2143,236,23,43,7,96,7,69,35,67,96]
print mergesort(blah)