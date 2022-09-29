class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr) - k
        
        while left < right:
            mid = (left + right) // 2
            midValue = arr[mid]
            
            if x - arr[mid+k] <= midValue - x:
                right = mid
            else:
                left = mid + 1
        
        return arr[left : left + k]