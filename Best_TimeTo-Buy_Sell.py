class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 0:
            return 0
        
        buy = prices[0]
        max_profit = 0
        
        for price in prices:
            if price < buy:
                buy = price
            elif price - buy > max_profit:
                max_profit = price - buy
        
        return max_profit

S=Solution()
prices=[7,6,4,3,1]
max_profit=S.maxProfit(prices)
print(max_profit)