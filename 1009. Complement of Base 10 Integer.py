class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum = 1
        while sum<n:
            sum = sum* 2+ 1
        return sum - n