#User function template for Python

class Solution:	
	def remove_duplicate(self, A, N):
	    cnt = 0
	    for i in range(N):
	        if A[cnt] != A[i]:
	            cnt += 1
	            A[cnt] = A[i]
	    return cnt+1


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        N = int(input())
        A = list(map(int, input().strip().split()))
        ob = Solution()
        n = ob.remove_duplicate(A,N)
        for i in range(n):
            print(A[i], end=" ")
        print()


# } Driver Code Ends