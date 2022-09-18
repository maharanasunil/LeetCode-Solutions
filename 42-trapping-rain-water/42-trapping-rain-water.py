class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0; r = len(height)-1
        res = 0
        leftMax = height[0]
        rightMax = height[-1]
        
        while l <= r:
            if height[l] <= height[r]:
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l] 
                l += 1
            else:
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
                r -= 1
        
        return res