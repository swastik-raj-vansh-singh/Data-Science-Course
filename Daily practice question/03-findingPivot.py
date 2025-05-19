# this approach is not handle 2 cases when pivot element is in oth index or in the last index
def pivot(l):
    n = len(l)
    start = 0
    end = n-1
    sum1 = 0
    sum2 = 0
    
    while (start < end):
        if (l[start] + sum1 == l[end] + sum2 ):
            return (start+1)
            
        elif (l[start]+sum1 < l[end] + sum2):
            sum1 += l[start]
            start += 1
        else:
            sum2 += l[end]
            end -= 1
    return -1

array = [1,3,2,5,6,8,3]
print (pivot(array))