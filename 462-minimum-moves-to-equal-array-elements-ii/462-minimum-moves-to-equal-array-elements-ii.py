class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return sum(abs(nums[i] - nums[n//2]) for i in range(n))