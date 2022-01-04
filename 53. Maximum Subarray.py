class Solution(object):
    def maxSubArray(self, nums):
        
        """
        :type nums: List[int]
        :rtype: int
        """
        s = []
        acc = 0
        for i in range(len(nums)):
            acc += nums[i]
            s.append(acc)
            
            if acc < 0:
                acc = 0
        return max(s)