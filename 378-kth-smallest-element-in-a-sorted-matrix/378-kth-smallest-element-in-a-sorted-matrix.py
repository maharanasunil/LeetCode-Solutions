class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def merge_two(a, b):
            (m, n) = (len(a), len(b))
            i = j = 0
            d = []
            while i < m and j < n:
                if a[i] <= b[j]:
                    d.append(a[i])
                    i += 1
                else:
                    d.append(b[j])
                    j += 1
            while i < m:
                d.append(a[i])
                i += 1
            while j < n:
                d.append(b[j])
                j += 1

            return d
        
        n=len(matrix)
        if n==1:
            return matrix[0][k-1]
        ans = list(merge(matrix[0],matrix[1]))
        for i in range(2,n):
            ans=list(merge(ans,matrix[i]))
        return ans[k-1]