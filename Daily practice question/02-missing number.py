def FindMissingNumber(l):
    n = len(l)
    total_sum = (n * (n+1))//2
    array_sum = sum(l)
    
    return (total_sum- array_sum)

array = [9,6,4,2,3,5,7,0,1]
print(FindMissingNumber(array))
