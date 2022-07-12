class Solution:
    def makesquare(self, arr: List[int]) -> bool:
        if sum(arr) % 4:
            return False
        
        side = sum(arr) // 4
        
        @lru_cache(None)
        def dp(k, mask, s):
            if k == 4:
                return True
            if not s:
                return dp(k+1, mask, side)
            
            for i in range(len(arr)):
                if mask & (1 << i) or s < arr[i]: continue
                if dp(k, mask ^ (1 << i), s - arr[i]):
                    return True
            return False
        
        return dp(0, 0, side)