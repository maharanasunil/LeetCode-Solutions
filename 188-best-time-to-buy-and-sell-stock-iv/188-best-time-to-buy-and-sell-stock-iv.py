class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k >= len(prices)//2: return sum(max(0, prices[i] - prices[i-1]) for i in range(1, len(prices)))
        ans = [0]*len(prices)
        for _ in range(k):
            most = 0
            for i in range(1, len(prices)):
                most = max(ans[i], most + prices[i] - prices[i-1])
                ans[i] = max(ans[i-1], most)
        return ans[-1]