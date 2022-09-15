class Solution(object):
    def findOriginalArray(self, changed):
        """
        :type changed: List[int]
        :rtype: List[int]
        """
        
        if len(changed) % 2 != 0:
            return []
        
        
        changed.sort()
        
        c = Counter(changed)
        
        answer = []
        
        for num in changed:
            if c[num] >= 1:
                c[num] -= 1
                if c[num * 2] >= 1:
                    answer.append(num)
                    c[num * 2] -= 1
                
            
        if len(answer) == len(changed) // 2:
            return answer
        
        return []