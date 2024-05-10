1.Write a program to find the sum of the given series 1+2+3+ . . . . . .(N terms)
Code:

class Solution:
    def seriesSum(self, n : int) -> int:
        add = n*(n+1)//2
        return add
# } Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        n = int(input())

        obj = Solution()
        res = obj.seriesSum(n)

        print(res)

# } Driver Code Ends
Explanation:
1. We have to find the sum of series of N terms.
2. For that we define a class Solution in which we define a function seriesSum.
3. We know that from basic mathematics the formula for sum of N terms is [N*(N+1)/2].We store the value in add variable.
4. Here to avoid floating point, we used floor division operator(//) in the formula.
5. Then we return the value to add as output.
