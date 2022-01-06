class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        for i, v in sorted(x for n, i, j in trips for x in [[i, n], [j, - n]]):
            capacity -= v
            if capacity < 0:
                return False
        return True