class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        # code from anubhabishere. Upvoted
        cur_sum, h = 0, []
        ans = -float('inf')
        
        # We sort the lists in order of decreasing performance so the current iteration efficiency is the smallest
        for i, j in sorted(zip(efficiency, speed),reverse=True):
            while len(h) > k-1:
                # we keep pushing all speed values but trim out the least values using heappop to fit the 'k' limit provided.
                cur_sum -= heappop(h)
            heappush(h, j)
            cur_sum += j
            # because we have trimmed out all values keeping 'k-1' number of values, we add current value and see if the efficiency penalty is worth its speed. The best answer is kept.
            ans = max(ans, cur_sum * i)
        
        return ans % (10**9+7)