class Solution:
    def merge(self, sk1, sk2):
        res = [[0,-1]]
        i, j , c= 0, 0, min(sk1[0][0], sk2[0][0])

        if sk1[0][0] < sk2[0][0]:
            sk2 = [[sk1[0][0], 0]] + sk2

        elif sk1[0][0] > sk2[0][0]:
            sk1 = [[sk2[0][0], 0]] + sk1

        while i < len(sk1) or j < len(sk2):

            if sk1[i][1] > sk2[j][1]:
                if sk1[i][1] != res[-1][1]:
                    res.append([c, sk1[i][1]])
            else:
                if sk2[j][1] != res[-1][1]:
                    res.append( [c, sk2[j][1]] )

            if i+1 < len(sk1) and (j+1 >= len(sk2) or sk1[i+1][0] < sk2[j+1][0] ): 
                    c = sk1[i+1][0]
                    i +=1

            elif j+1 < len(sk2) and (i+1 >= len(sk1) or sk1[i+1][0] > sk2[j+1][0]):
                    c = sk2[j+1][0]
                    j +=1

            elif i+1 < len(sk1) and j+1 < len(sk2) and sk1[i+1][0] == sk2[j+1][0]:
                c = sk1[i+1][0]
                i+=1
                j+=1

            else:
                i+=1
                j+=1

        res.pop(0)
        return res


    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:

        if len(buildings) == 1:
            return [[buildings[0][0], buildings[0][2]], [buildings[0][1], 0] ]

        if len(buildings) == 0:
            return []
        
        n = len(buildings)//2
        a = buildings[:n] 
        b = buildings[n:]

        return self.merge(self.getSkyline(a), self.getSkyline(b))