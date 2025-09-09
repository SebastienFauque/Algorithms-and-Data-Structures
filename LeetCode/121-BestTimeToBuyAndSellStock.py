class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        spread = 0
        minNum = prices[0]
        for num in prices[1:]:
            if num < minNum:
                minNum = num
            
            spread = max(spread, num - minNum)
        
        return spread