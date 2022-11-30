class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d, ans = {}, []
        for n in arr:
            if n not in d: d[n] = 1
            else: d[n] += 1
        for n in d: ans.append(d[n])
        return sorted(ans) == sorted(set(ans))    