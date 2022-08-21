class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sums = 0
        product = 1
        for i in str(n):
            num = int(i)
            sums += num
            product *= num
        return product-sums