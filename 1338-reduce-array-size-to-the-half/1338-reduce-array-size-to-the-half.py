class Solution:
    def minSetSize(self, A: List[int]) -> int:
        L, C = len(A), collections.Counter(A)
        S = sorted(C.values(), reverse = True)
        T = itertools.accumulate(S)
        for i,v in enumerate(T):
            if v >= len(A)//2: return i + 1