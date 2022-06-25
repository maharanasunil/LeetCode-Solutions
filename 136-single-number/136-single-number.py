class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans = ans^num # XOR of the entire Array
        return ans

#Properties of XOR
#1: a^0 = a
#2: a^a = a
#3: a^b = b^a