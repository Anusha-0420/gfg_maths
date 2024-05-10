Given two numbers A and B. Your task is to return the sum of A and B.

code:
class Solution:
    def addition (ob,A,B):
        # code here 
        return A+B

if __name__ == '__main__': 
    t = int (input())
    for _ in range (t):
        
        A,B=map(int,input().strip().split(" "))

        ob = Solution()
        print(ob.addition(A,B))
Explanation: 
1. The Solution class is defined, which presumably contains methods for solving specific problems.
2. The addition method takes three arguments: self (indicating that this method is part of a class), and two integers: A and B.
3. It calculates the sum of A and B using the + operator.
4. The method returns the result of the addition.
5. The code reads an integer t (presumably the number of test cases) and iterates through each test case:
  a) For each test case, it reads two integers: A and B.
  b) An instance of the Solution class is created.
  c) The addition method is called with the input integers A and B.
  d) The result (the sum of A and B) is printed for each test case.
