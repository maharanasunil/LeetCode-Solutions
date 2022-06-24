class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        minSoFar = prices[0]
        for  i in range(1, len(prices)):
            currProfit = prices[i] - minSoFar
            if currProfit > ans:
                ans = currProfit
            minSoFar = min(minSoFar, prices[i])
        return ans