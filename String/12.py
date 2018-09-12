class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        
        numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        output  = ''
        if num in values:
            
            return numerals[values.index(num)]
        for i in range(0,len(values)):
            q = num//values[i]
            if q > 0:
                output += numerals[i] * q
                num-= values[i]
                print('ff')
        return output
