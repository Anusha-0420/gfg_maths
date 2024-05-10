Given a number, reverse it and add it to itself unless it becomes a palindrome or number of iterations becomes more than 5.
Code: 
class Solution:
    def reverse(self,n):
        rev=0
        while(n>0):
            rev=rev*10+n%10
            n=int(n/10)
        return rev
    def isSumPalindrome (self, n):
        # code here 
        for i in range(6):
            if n==self.reverse(n):
                return n
            n=self.reverse(n)+n
        return -1

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        
        ob = Solution()
        print(ob.isSumPalindrome(n))
Explanation: 
1. The Solution class is defined, which presumably contains methods for solving specific problems.
2. The reverse method takes two arguments: self (indicating that this method is part of a class) and an integer n.
3. It reverses the digits of the integer n using a loop:
  a) Initialize rev to 0.
  b) While n is greater than 0:
    (1) Multiply rev by 10 and add the last digit of n (obtained using n % 10).
    (2) Update n by removing the last digit (using n = int(n / 10)).
  c) Return the reversed integer.
4. The isSumPalindrome method takes two arguments: self and an integer n.
5. It checks whether the sum of n and its reverse is a palindrome (i.e., the same when read backward).
6. It iterates through the process up to 6 times:
  a) If n is equal to its reverse, it returns n.
  b) Otherwise, it updates n by adding its reverse.
7. If no palindrome is found after 6 iterations, it returns -1.
8. The code reads an integer t (presumably the number of test cases) and iterates through each test case:
  a) For each test case, it reads an integer n.
  b) An instance of the Solution class is created.
  c) The isSumPalindrome method is called with the input integer n.
  d) The result (either a palindrome or -1) is printed for each test case.
