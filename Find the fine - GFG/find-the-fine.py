#User function Template for python3

class Solution:
    def totalFine(self, n, date, car, fine):
        total = 0
        if date%2 == 0:
            for i in range(n):
                if car[i]%2 == 1:
                    total += fine[i]
        else:
            for i in range(n):
                if car[i]%2 == 0:
                    total += fine[i]
        return total
    
    
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n, k = [int(x) for x in input().strip().split()]
        arr = [int(x) for x in input().strip().split()]
        brr = [int(x) for x in input().strip().split()]
        
        print(Solution().totalFine( n, k, arr, brr))

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends