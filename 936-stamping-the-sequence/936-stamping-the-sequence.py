class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        N,M = len(target),len(stamp)
        move = 0
        maxmove = 10*N
        ans = []
        def check(string):
            for i in range(M):
                if string[i] == stamp[i] or string[i] == '?':
                    continue
                else:
                    return False
            return True
        
        while move < maxmove:
            premove = move
            for i in range(N-M+1):
                if check(target[i:i+M]):
                    move += 1
                    ans.append(i)
                    target = target[:i] + "?"*M + target[i+M:]
                    if target == "?"*N : return ans[::-1]
            if premove == move:return []
        return []