class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and not num & (num - 1)  and len(bin(num)) % 2 
    
        # Time Limit Exceeded
        #i = 0
        #curr = 0
        #while i <= n:
        #    curr = 4 ** i
        #    if curr == n:
        #        return True
        #    i += 1
        #return False