class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
       
        if len(prices) == 0:
            return 0
        min_ = prices[0]
        profit = 0
        min_i = 0
        for i,p in enumerate(prices):

            if min_ > p :
                min_ = p
            elif p - min_ > profit :
                profit = p - min_
        return profit