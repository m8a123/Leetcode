class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        curr_min = float('inf')
        for i in range(len(prices)):
            curr_min = min(curr_min, prices[i])
            max_profit = max(max_profit, prices[i] - curr_min)
        return max_profit 

