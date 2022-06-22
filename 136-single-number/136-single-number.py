class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict = {}
        for num in nums:
            dict[num] = dict.get(num, 0) + 1
        for key, value in dict.items():
            if value == 1:
                return key