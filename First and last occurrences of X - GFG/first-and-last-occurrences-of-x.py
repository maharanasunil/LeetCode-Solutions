#User function Template for python3
class Solution: 
    def firstAndLast(self, arr, n, x): 
        if x not in arr:
            return [-1]
        result = []
        for i in range(n):
            if arr[i] == x:
                result.append(i)
        return [result[0], result[0]] if len(result) == 1 else [result[0], result[-1]]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input()) 
    for _ in range(t):
        n,x = [int(i) for i in input().split()] 
        arr = [int(i) for i in input().split()] 
        ob=Solution() 
        ans=ob.firstAndLast(arr,n,x) 
        s=(" ").join(map(str,ans))
        print(s)

# } Driver Code Ends