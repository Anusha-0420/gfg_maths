Given 3 numbers A, B and C. Find the greatest number among them.
  code:

class Solution:
    def greatestOfThree(self,A,B,C):
        #code here
        return max(A,B,C)

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        A,B,C=map(int,input().strip().split(' '))
        ob=Solution()
        print(ob.greatestOfThree(A,B,C))   
Explanation: 
1. The Solution class is defined, which presumably contains methods for solving specific problems.
2. The greatestOfThree method takes four arguments: self (indicating that this method is part of a class), and three integers: A, B, and C.
3. It calculates the maximum value among the three input integers using the max() function.
4. The method returns the maximum value.
5. The code reads an integer t (presumably the number of test cases) and iterates through each test case:
  a) For each test case, it reads three integers: A, B, and C.
  b) An instance of the Solution class is created.
  c) The greatestOfThree method is called with the input integers A, B, and C.
  d) The maximum value is printed for each test case.
However, there are a few things to note:

The code assumes that the input format is as described (number of test cases followed by the integer values).
It does not handle invalid inputs or edge cases.
