class Solution:
    def climbStairs(self, n: int) -> int:
        self.ht = {}
        return self.f(0, n)
        
    def f(self, i, n):
        if (i > n):
            return 0
        elif (i == n):
            return 1
        else:
            if i in self.ht:
                return self.ht[i]
            else:
                self.ht[i] = self.f(i+1, n) + self.f(i+2, n)
                return self.ht[i]