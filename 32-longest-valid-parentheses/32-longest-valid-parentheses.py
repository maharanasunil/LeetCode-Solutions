class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [0]
        longest = 0
        
        for i in s:
            if i == '(':
                stack.append(0)
            elif len(stack)>1:
                val = stack.pop()
                stack[-1] += val+2
                longest = max(longest, stack[-1])
            else:
                stack = [0]
        return longest