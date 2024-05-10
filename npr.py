Write a program to calculate nPr. nPr represents n permutation r and value of nPr is (n!) / (n-r)!.
  code: 

class Solution:
    def factorial(self,a):
        if a==0 or a==1:
            return 1
        else:
            return a*self.factorial(a-1)
            
    def nPr(self, n, r):
        # code here
        fact_1 = self.factorial(n)
        fact_2 = self.factorial(n-r)
        return(fact_1//fact_2)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, r = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.nPr(n, r))
Explanation:
1. The Solution class is defined, which presumably contains methods for solving specific problems.
2. The factorial method calculates the factorial of a given integer a. If a is 0 or 1, it returns 1. Otherwise, it recursively computes a!.
3. The nPr method calculates the permutation of n items taken r at a time. 
4. It uses the formula: nPr= n!/(n−r)!​
5. The code reads an integer t (presumably the number of test cases) and iterates through each test case:
                                                                                     
  a) For each test case, it reads two integers: n and r.
  b) An instance of the Solution class is created.
  c) The nPr method is called with the input integers n and r.
  d) The result (the value of nPr) is printed for each test case.

However, there are a few things to note:

The code assumes that the input format is as described (number of test cases followed by pairs of integers).
It does not handle invalid inputs or edge cases (e.g., negative values for n or r).

