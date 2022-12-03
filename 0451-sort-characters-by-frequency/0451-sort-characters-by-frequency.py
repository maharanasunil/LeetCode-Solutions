class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
            
        sort_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        
        return ''.join(x[0]*x[1] for x in sort_freq)