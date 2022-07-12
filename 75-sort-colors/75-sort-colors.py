class Solution:
    def sortColors(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(arr) - 1
        
        i = 0
        while(i <= right):
            if (arr[i] == 0):
                (arr[i], arr[left]) = (arr[left], arr[i])
                left += 1
                i += 1
            elif (arr[i] == 2):
                (arr[i], arr[right]) = (arr[right], arr[i])
                right -= 1
            else:
                i += 1