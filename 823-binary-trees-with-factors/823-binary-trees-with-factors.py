class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        As = set(A) # set for O(1) lookup 
        pq = [] # min heap 
        for x, y in product(A, A): 
            if x*y in As: heappush(pq, (x*y, x, y))
        
        cnt = {x: 1 for x in A}
        while pq: 
            z, x, y = heappop(pq)
            cnt[z] += cnt[x] * cnt[y]
        
        return sum(cnt.values()) % 1_000_000_007