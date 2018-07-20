def maxDistToClosest( seats):
    """
    :type seats: List[int]
    :rtype: int
    """
    count_zero = 0
    previous = -1
    output = 0
    for i,seat in enumerate(seats):
        if seat == 0  :
            count_zero +=1
        elif seat == 1 or i == len(seats):
  
            if count_zero // 2 == 0:
                output_ = 
            else:
                output = count_zero/2 
            count_zero = 0
    return  output

seats = [1,0,0,0]
print(maxDistToClosest(seats))
