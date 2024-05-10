You are given an integer N, reverse the digits of given number N, ensuring that the reversed number has no leading zeroes. Return the resulting reversed number.
Code: 

class Solution:
	def reverse_digit(self, n):
	    
        rev = ''.join(reversed(str(n)))
        return int(rev)

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.reverse_digit(n)
		print(ans)

Explanation:

1. The Solution class is defined, which presumably contains methods for solving specific problems.
2. The reverse_digit method takes two arguments: self (indicating that this method is part of a class) and an integer n.
3. It converts the integer n to a string using str(n).
4. It reverses the characters in the string using the reversed() function and joins them back together using join().
5. The reversed string is then converted back to an integer using int(rev).
6. The method returns this reversed integer.
7. The code reads an integer T (presumably the number of test cases) and iterates through each test case:

a) For each test case, it reads an integer n.
b) An instance of the Solution class is created.
c) The reverse_digit method is called with the input integer n.
d) The reversed integer is printed for each test case.
However, there are a few things to note:

The code assumes that the input format is as described (number of test cases followed by the integer values).
It does not handle invalid inputs or edge cases (e.g., negative numbers).
