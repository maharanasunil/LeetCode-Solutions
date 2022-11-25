class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        res = 0
        stack = [-1]                                        # We are adopting increasing stack to solve this problem.
        arr += [0]                                          # The trick is as same as problem 84,
                                                            # put 0 in the last of arr, also keeping stack[0] always the smallest element without affecting res.
            
            
        for i in range(len(arr)):                           
            while arr[i] < arr[stack[-1]]:                  
                mid = stack.pop()                           # mid is the idx of "num" which is the smallest element in current interval.  
                num = arr[mid]
                right = i                                   # "right" is the right first element smaller than "num"
                left = stack[-1]                            # "left" is the left first element smaller than "num"
                res += num * (right-mid) * (mid-left)
            stack.append(i)
        
        return res % (10**9 + 7)