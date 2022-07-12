class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        res = []
        for i in range(len(nums)):
            ans = 1
            for j in range(len(nums)):
                if i != j:
                    ans = ans*nums[j]
                elif i == j:
                    continue
            res.append(ans)
        return res
        """        
        left = [1]
        n = len(nums)
        for i in range(1, n):
            left.append(left[i-1]*nums[i-1])
            
        right = [1]*(n+1)
        for i in range(n-2, -1, -1):
            right[i] = right[i+1]*nums[i+1]
            
        result = []
        for i in range(n):
            result.append(left[i]*right[i])
        
        return result