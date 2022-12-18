class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0] * len(T)
        stack = []
        
        for index in range(len(T)-1, -1, -1):
            
            while stack and T[stack[-1]] <= T[index]:
                stack.pop()
                        
            res[index] = stack[-1] - index if stack else 0
            
            stack.append(index)

            
        return res