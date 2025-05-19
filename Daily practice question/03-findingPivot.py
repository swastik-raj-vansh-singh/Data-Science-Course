def pivot(l):
    n = len(l)
    start = 0
    end = n-1
    sum1 = 0
    sum2 = 0
    first  = sum(l) - l[0]
    last = sum(l) - l[n-1]

    if sum(l[1:]) == 0:
        return 0
    
    while (start < end):
        if first == 0:
            return 0
        if last == 0:
            return n-1
            
        elif (l[start] + sum1 == l[end] + sum2 ):
            return (start+1)
            
        elif (l[start]+sum1 < l[end] + sum2):
            sum1 += l[start]
            start += 1
        else:
            sum2 += l[end]
            end -= 1
    return -1

array = [0,0,0, 0]
print (pivot(array))


