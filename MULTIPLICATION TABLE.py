Create the multiplication table of a given number N and return the table as an array.
  code:
class Solution:
    def getTable(self,N):
        # code here
        op=[]
        for i in range(1,11):
            product = N*i
            op.append(product)

        return op

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.getTable(N)
        for i in ans:
            print(i,end=" ")
        print()
Explanation: 
1. The Solution class is defined, which presumably contains methods for solving specific problems.
2. The getTable method takes two arguments: self (indicating that this method is part of a class) and an integer N.
3. It initializes an empty list called op.
4. The code iterates through the numbers from 1 to 10 (inclusive) using range(1, 11).
5. For each number i, it calculates the product of N and i and appends it to the op list.
6. The method returns the list op.
7. The code reads an integer t (presumably the number of test cases) and iterates through each test case:
  a) For each test case, it reads an integer N.
  b) An instance of the Solution class is created.
  c) The getTable method is called with the input integer N.
  d) The resulting list of products is printed, with each value separated by a space.
However, there are a few things to note:

The code assumes that the input format is as described (number of test cases followed by the integer values).
It does not handle invalid inputs or edge cases.
