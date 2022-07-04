class Solution:
    def candy(self, ratings: List[int]) -> int:
        lenratings = len(ratings)       # call len only once. It is used 3 times
        ans = [1] * lenratings
        for i in range(1, lenratings):
            if ratings[i] > ratings[i-1]:
                ans[i] = ans[i-1] + 1
        for i in range(lenratings-2, -1, -1):
            a = i+1                     # a is used 2 times in if
            # compare rantings and candys is faster than use "max" to calculate.
            if ratings[i] > ratings[a] and ans[i] <= ans[a]:
                ans[i] = ans[a] + 1
        return sum(ans)