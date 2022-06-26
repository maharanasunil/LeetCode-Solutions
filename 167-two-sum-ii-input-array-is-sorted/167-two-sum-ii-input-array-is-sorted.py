class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left_pointer = 0
        right_pointer = len(nums) - 1
        while(left_pointer < right_pointer):
            currentSum = nums[left_pointer] + nums[right_pointer]
            if (currentSum < target):
                left_pointer += 1
            elif (currentSum > target):
                right_pointer -= 1
            else:
                return [left_pointer+1, right_pointer+1]
        return []