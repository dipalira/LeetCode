#Binary Search Implementation
class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0,len(numbers)):
            x = target - numbers[i]
            start = i + 1
            end = len(numbers)-1
            while start <= end:
                mid = start + (end -start)//2
                #print(mid)
                if numbers[mid] == x:
                    return [i+1, mid+ 1]
                    break
                elif numbers[mid] > x:
                    end = mid -1
                elif numbers[mid] < x:
                    start = mid + 1 
##################################################################################################

##############################################################################################
#Dictionary Implementation


class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i,num in enumerate(numbers):
            temp = target - num
            if temp in dic:
                return [dic[temp] +1, i+1]
            else:
                dic[num] = i
