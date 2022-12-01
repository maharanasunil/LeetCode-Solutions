class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set('aeiouAEIOU')
        count = 0
        for i in range(len(s)//2):
            if s[i] in vowels:
                count+=1
            if s[-i-1] in vowels:
                count-=1

        return count == 0