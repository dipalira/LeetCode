###################3 Insertion Sort   #############################
# Function to do insertion sort
def insertionSort(arr):
 
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
 
        key = arr[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i -1
        while j>=0  :
        	if key < arr[j]:
        		arr[j+1] = arr[j]
        		arr[j] = key
        		j -= 1
        	else: 
        		break
    print(arr)
arr =[ 9 ,7 ,8 ,12, 10]


#insertionSort(arr)

############################################

def msort3(x):
    result = []
    if len(x) < 2:
        return x
    mid = int(len(x) / 2)
    y = msort3(x[:mid])

    z = msort3(x[mid:])
    i = 0
    j = 0
    while i < len(y) and j < len(z):
        if y[i] > z[j]:
            result.append(z[j])
            j += 1
        else:
            result.append(y[i])
            i += 1
    result += y[i:]
    result += z[j:]
    return result
#########################################################

def msort4(x):
    # Base Case
    if len(x) == 1: return x
    #Left array
    mid = int(len(x/2))
    left = msort4(x[:mid])
    right = msort4(x[mid:])
    while(len(left) > 0 and len(right)>0):
        if left[0] > right[0]:
            result.append(right[0])
            right.pop(0)
        else:
            result.append(left[0])
            left.pop(0)
    result.extend(left)
    result.extend(right)
    return result