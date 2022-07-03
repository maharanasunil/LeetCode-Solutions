class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        memo={}
        def recurse(index,state):
            if index==len(nums):
                return 0
            if index in memo:
                return memo[index]
            ans=1
            for i in range(index+1,len(nums)):
                if state=='positive' and nums[i]-nums[index]<0:
                    ans=max(ans,1+recurse(i,'negative'))
                elif state=='negative'and nums[i]-nums[index]>0:
                    ans=max(ans,1+recurse(i,'positive'))
            memo[index]=ans
            return memo[index]
        res=float('-inf')
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]>0:
                res=max(res,1+recurse(i,'positive'))
            elif nums[i]-nums[i-1]<0:
                res=max(res,1+recurse(i,'negative'))
        if res==float('-inf'):
            return 1
        return res