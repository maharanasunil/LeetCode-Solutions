# Time: O(n)
# Space: O(n), In order to set up O(1) containment lookups, we allocate linear space for a hash table to store the O(n) numbers in nums.
class Solution:
	def longestConsecutive(self, nums: List[int]) -> int:
		if not nums:
			return 0
		maxCons = -(1 << 31)
		nums = set(nums)
		for num in nums:
			if num-1 not in nums:
				cur = num
				count = 1
				while cur+1 in nums:
					cur += 1
					count += 1
				maxCons = max(count, maxCons)
		return maxCons