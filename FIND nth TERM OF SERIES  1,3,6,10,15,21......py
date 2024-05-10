Given a number N, find the Nth term in the series 1, 3, 6, 10, 15, 21…
Code: 
class Solution:
    def findNthTerm(self, N):
        # code here
        return N*(N+1)//2

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.findNthTerm(N))

Explanation: 
1. The Solution class is defined, which presumably contains methods for solving specific problems.
2. The findNthTerm method takes two arguments: self (indicating that this method is part of a class) and an integer N.
3. It calculates the N-th term of a sequence using the formula: 
      N⋅(N+1)/2​

4. The method returns the calculated value.
5. The code reads an integer t (presumably the number of test cases) and iterates through each test case:
  a) For each test case, it reads an integer N.
  b) An instance of the Solution class is created.
  c) The findNthTerm method is called with the input integer N.
  d) The result (the N-th term) is printed for each test case.
