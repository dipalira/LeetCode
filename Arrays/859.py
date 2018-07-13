def maxDistToClosest( seats):
    """
    :type seats: List[int]
    :rtype: int
    """
    count_zero = 0
    previous = -1
    output = 0
    
    for i,seat in enumerate(seats):
        if seat == 0 :
            count_zero +=1
            j = 0
        elif seat == 1 :
            j = 1  
            output = max(output, int(count_zero/2) )
            print("Not 1",output )
            count_zero = 0
            
        if seat == 0 and (i == len(seats)-1):
            print("Not 2",count_zero , output)
            output = max(output, count_zero - 1) 

        #print(count_zero,i)
    if output // 2 == 0:
        return output
    else:
        return  output + 1

seats =  [1,0,0,0,1,0,1]
#print(len(seats)-1)
print(maxDistToClosest(seats))