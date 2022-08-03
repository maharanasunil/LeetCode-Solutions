class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sums = 0
        for i in str(n):
            digit = int(i)
            product *= digit
            sums += digit
        return product - sums