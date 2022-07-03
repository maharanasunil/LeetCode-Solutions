class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for ele in nums:
            if ele not in dict:
                dict[ele] = 1
            else:
                return True
        return False