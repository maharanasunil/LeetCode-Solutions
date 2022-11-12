class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []
        
    def addNum(self, num: int) -> None:
        if not self.nums:
            self.nums.append(num)
            return 
        l = 0
        r = len(self.nums)-1
        while l < r:
            m = (l+r)//2
            if self.nums[m] == num:
                self.nums.insert(m,num)
                return 
            elif self.nums[m] < num:
                l = m+1
            else:
                r = m-1      
        if self.nums[l] < num:
            self.nums.insert(l+1,num)
        else:
            self.nums.insert(l,num)

    def findMedian(self) -> float:
        mid = (0 + len(self.nums)-1 )//2
        if (len(self.nums)-1) & 1:
            return (self.nums[mid] + self.nums[mid+1])/2
        else:
            return self.nums[mid]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()