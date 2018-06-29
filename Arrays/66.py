class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        output = ''
        for i in digits:
            output += str(i)
        
        output_ = int(output)
        output_ += 1
        return  [ int(i) for i in str(output_)]       
