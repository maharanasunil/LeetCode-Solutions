class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = 0
        
        if (len(nums) == 1):
            return nums[0]
        
        currentProduct = 1
        for ele in nums:
            if(ele != 0):
                currentProduct = currentProduct*ele
                ans = max(ans, currentProduct)
            else:
                currentProduct = 1
        
        currentProduct = 1
        for i in range(len(nums)-1, -1, -1):
            if(nums[i] != 0):
                currentProduct = currentProduct*nums[i]
                ans = max(ans, currentProduct)
            else:
                currentProduct = 1
                
        return ans