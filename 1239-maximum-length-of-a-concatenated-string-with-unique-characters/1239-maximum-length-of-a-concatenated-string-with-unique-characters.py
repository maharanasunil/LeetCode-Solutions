class Solution:
    def subSequences(self, arr, index, temp):
        if index == len(arr):
            # Remove concatenated items that have duplicate chars
            if len(temp) == len(set(temp)):
                return len(temp)
            else:
                return -1
        else:
            return max(
                self.subSequences(arr, index + 1, temp + arr[index]),
                self.subSequences(arr, index + 1, temp))

    def maxLength(self, arr: List[str]) -> int:
        arrNew = []
        for a in arr:
            # Remove items that have duplicate chars
            if len(a) == len(set(a)):
                arrNew.append(a)
        return self.subSequences(arrNew, 0, '')