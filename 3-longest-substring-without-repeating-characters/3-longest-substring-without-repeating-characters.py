class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = defaultdict(int)        # track counts of each character
        l=0
        max_length=0
        for r, c in enumerate(s):
            counter[c]+=1            
            if counter[c] > 1:                
                while l<r and counter[c]>1: # iterate until window is valid
                    counter[s[l]]-=1
                    l+=1
            max_length=max(max_length, r-l+1)
        return max_length