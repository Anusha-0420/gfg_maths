Given a single integer N, your task is to find the sum of the square of the first N even natural Numbers.
Code:
class Solution:
	def sum_of_square_evenNumbers(self, n):
		return ((2*n)*(n+1)*((2*n)+1))//3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.sum_of_square_evenNumbers(n)
		print(ans)
Explanation: 
1. The Solution class contains a method called sum_of_square_evenNumbers.
2. Given an integer n, it calculates the sum of squares of even numbers from 2 to n.
3. The formula used is: 
      Sum of squares of even numbers: 2n⋅(n+1)⋅(2n+1)/3​
4. The code reads an integer T (number of test cases) and iterates through each test case:

  a) For each test case, it reads an integer n.
  b) An instance of the Solution class is created.
  c) The sum_of_square_evenNumbers method is called with the input integer n.
  d) The result (the sum of squares of even numbers) is printed for each test case.
