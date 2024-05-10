Given a positive integer N, determine whether it is odd or even.
  code:

class Solution:
    def oddEven (ob,N):
        # code here 
        
        if N%2 == 0:
            return "even"
        else:
            return 'odd'

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N=int(input())

        ob = Solution()
        print(ob.oddEven(N))
Explanation:
1. The Solution class is defined, which presumably contains methods for solving specific problems.
2. The oddEven method takes two arguments: self (indicating that this method is part of a class) and an integer N.
3. It checks whether N is even or odd:
  a) If N is even (i.e., N % 2 == 0), it returns the string “even.”
  b) Otherwise (when N is odd), it returns the string “odd.”
4. The code reads an integer t (presumably the number of test cases) and iterates through each test case:
  a) For each test case, it reads an integer N.
  b) An instance of the Solution class is created.
  c) The oddEven method is called with the input integer N.
  d) The result (either “even” or “odd”) is printed for each test case.
However, there are a few things to note:

The code assumes that the input format is as described (number of test cases followed by the integer values).
It does not handle invalid inputs or edge cases (e.g., negative numbers).
