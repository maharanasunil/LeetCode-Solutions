#User function Template for python3


class Solution:
    def MissingNumber(self,array,n):
        # total = n*(n+1)//2
        # given_sum = 0
        # for num in array:
        #     given_sum += num
        # return total-given_sum
        sum1 = sum([i for i in range(n+1)])
        givenSum = 0
        for i in array:
            givenSum += i
        return sum1 - givenSum

#{ 
 # Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().MissingNumber(a,n)
    print(s)
# } Driver Code Ends