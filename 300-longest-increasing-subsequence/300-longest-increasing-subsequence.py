class Solution:
	def lengthOfLIS(self, nums: List[int]) -> int:
		n = len(nums)
		dp = [0]*n
		for i in range(n):
			maX = 0
			for j in range(i+1):
				if nums[j] < nums[i]:
					if dp[j] > maX:
						maX = dp[j]
			dp[i] = maX+1
		return max(dp)