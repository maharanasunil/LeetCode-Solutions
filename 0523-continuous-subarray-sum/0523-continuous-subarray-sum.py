class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_sums = defaultdict(lambda:float(inf))        
        #Key is prefix_sum%k, value is earliest occurence of the same prefix_sum   
        
        running_sum = 0
        for i, n in enumerate(nums):
            running_sum += n
            mod_sum = running_sum%k
            #If running_sum%k = 0 + other_sum%k for a value other_sum in prefix_sum 
            #then we can subtract the other_sum and we'll have a multiple of k
            
            #Subarray must have at least 2 elements so we will not return True in cases of having just one element
            #or subtracting the prefix_sum right before the current one
            if i >= 1 and (mod_sum == 0 or prefix_sums[mod_sum] < i - 1):
                return True
            
            #We wouldn't need to keep track of minimum position if we could have subarray of size 1
            prefix_sums[mod_sum] = min(prefix_sums[mod_sum], i)
                
        return False