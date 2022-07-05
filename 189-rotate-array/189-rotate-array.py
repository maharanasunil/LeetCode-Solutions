class Solution:
    
    def reverse_array(self, nums: List[int], start: int, end: int) -> None:
        l = start
        r = end - 1
        while(l < r):
            (nums[l], nums[r]) = (nums[r], nums[l])
            l += 1
            r -= 1
        
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        self.reverse_array(nums, 0, len(nums))
        self.reverse_array(nums, 0, k)
        self.reverse_array(nums, k, len(nums))