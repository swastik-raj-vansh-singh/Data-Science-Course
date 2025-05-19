def MovingZeroToTheLast(l):
    fast = 0
    slow = 0
    n = len(l)
    while(fast < n):
        if l[fast] !=0 :
            l[slow] = l[fast]

            # have to handle this case 
            if slow != fast:
                l[fast] = 0

            slow += 1
            fast +=1
        else:
            fast +=1
    return l
        

array  = [0,1,0,3,12]
array1 = [1,0,0,2,2]
l = MovingZeroToTheLast(array1)
print (l)