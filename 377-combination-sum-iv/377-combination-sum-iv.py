class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        '''
            Here we are doing bottom up DP and the base case would be =>
            when target is zero how many way can we achieve that: 1 way
        '''
        dp = { 0 : 1 } # base case 
        for total in range(1,target+1):
            dp[total] = 0
            for n in nums:
                dp[total] += dp.get(total-n,0)
        return dp[target]