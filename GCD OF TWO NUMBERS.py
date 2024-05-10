Given two positive integers a and b, find GCD of a and b. write a python code without using inbuilt GCD function
  code: 
class Solution:
    def gcd(self, a : int, b : int) -> int:
        # code here
        if a<b:
            a,b = b,a
        if b==0:
            return a
        else:
            return self.gcd(b,a%b)

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a = int(input())
        
        
        b = int(input())
        
        obj = Solution()
        res = obj.gcd(a, b)
        
        print(res)
explanation: 
1. The Solution class is defined, which presumably contains methods for solving specific problems.
2. The gcd method takes three arguments: self (indicating that this method is part of a class), an integer a, and an integer b.
3. It calculates the greatest common divisor (GCD) of a and b using the Euclidean algorithm.
4. The algorithm ensures that a is greater than or equal to b.
5. If b is 0, it returns a as the GCD.
6. Otherwise, it recursively calls itself with arguments b and a % b.
7. The code reads an integer t (presumably the number of test cases) and iterates through each test case:
  a) For each test case, it reads two integers a and b.
  b) An instance of the Solution class is created.
  c) The gcd method is called with the input integers a and b.
  d) The GCD result is printed for each test case.
However, there are a few things to note:

The code assumes that the input format is as described (number of test cases followed by pairs of integers).
It does not handle invalid inputs or edge cases (e.g., negative numbers).
