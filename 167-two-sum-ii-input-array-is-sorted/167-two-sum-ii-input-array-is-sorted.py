class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        f = 0
        s = len(nums) - 1
        while(f < s):
            currentSum = nums[f] + nums[s]
            if (currentSum < target):
                f += 1
            elif (currentSum > target):
                s -= 1
            else:
                return [f+1, s+1]