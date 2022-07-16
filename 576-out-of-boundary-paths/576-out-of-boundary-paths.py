class Solution:         # The plan is to accrete the number of paths from the starting cell, which
                        # is the sum of (a) the number of adjacent positions that are off the grid
                        # plus (b) the number of paths from the adjacent cells in the grid within 
                        # maxMove steps. We determine (b) recursively.

    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:

        @lru_cache(None)                                # <-- Many cells are revisted so we cache the previous calls
        def dp (x,y,steps = maxMove):
            if x not in range(m) or y not in range(n):  # <-- Moved off the grid so increment the tally
                return 1
            if not steps:                               # <-- Ran out of the maxMove steps
                return 0

            ans, dx, dy = 0, 1, 0
            for _ in range(4):
                ans+= dp(x+dx, y+dy, steps-1)           # <-- visit the adjacent cells
                dx, dy = dy,-dx                         # <-- iterates thru the directions:
				                                        #         south => east => north => west 

            return ans  

        return dp (startRow, startColumn)%1000000007
		
		# Thanks to XixiangLiu for fixing a number of my errors in the original post.