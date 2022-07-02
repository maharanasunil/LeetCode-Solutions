class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        acc = 0
        res = []
        for i in nums:
            acc = acc + i
            res.append(acc)
            
            if acc < 0:
                acc = 0
        return max(res)
            