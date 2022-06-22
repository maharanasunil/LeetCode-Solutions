class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        less = []
        greater = []
        pivot = nums.pop()
        for num in nums:
            if num < pivot:
                less.append(num)
            else:
                greater.append(num)
        
        if len(greater)+1 == k:
            return pivot
        elif len(greater)+1 > k:
            return self.findKthLargest(greater, k)
        else:
            return self.findKthLargest(less, k-len(greater)-1)      