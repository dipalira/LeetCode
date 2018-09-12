class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum_,prev = 0,0 
        romans = {'M': 1000, 'D': 500 , 'C': 100, 'L': 50, 'X': 10,'V': 5,'I': 1}
        for i in range(len(s) - 1, -1 ,-1):

            #Decreasing Case
            if romans[s[i]] < prev:
                #Subtract 
                sum_ -= romans[s[i]]
            else:
                sum_ += romans[s[i]]
            prev = s[i]
        return sum_
