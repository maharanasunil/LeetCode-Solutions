class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = 'L' + dominoes + 'R'
        res = []
        left = 0
        
        for right in range(1, len(dominoes)):
            if dominoes[right] == '.': 
                continue
                
            middle = right - left - 1
            if left: 
                res.append(dominoes[left])
            if dominoes[left] == dominoes[right]: 
                res.append(dominoes[left] * middle)
            elif dominoes[left] == 'L' and dominoes[right] == 'R':
                res.append('.' * middle)
            else: 
                res.append('R' * (middle // 2) + '.' * (middle % 2) + 'L' * (middle // 2))
            left = right
            
        return ''.join(res)