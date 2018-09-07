class Solution:
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if a == b:
            return -1
        elif len(a) == len(b):
            return len(a)
        elif len(a) != len(b):
            return max(len(a),len(b))
        
