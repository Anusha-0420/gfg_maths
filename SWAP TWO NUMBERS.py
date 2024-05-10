Swap given two numbers and print them (Try to do it without a temporary variable.) and return it.
Code:
class Solution:
    def get(self, a, b):
        #code here
        return b,a 

if __name__ == "__main__":
	t = int (input ())
	for tc in range (t):
		a,b = map(int,input().strip().split())
		ob = Solution()
		ans=ob.get(a,b)
		print(str(ans[0])+" "+str(ans[1]))
Explanation:
1. The Solution class is defined, which presumably contains methods for solving specific problems.
2. The get method takes three arguments: self (indicating that this method is part of a class), and two integers: a and b.
3. It returns a tuple with the values of b and a swapped (i.e., (b, a)).
4. The code reads an integer t (presumably the number of test cases) and iterates through each test case:
  a) For each test case, it reads two integers: a and b.
  b) An instance of the Solution class is created.
  c) The get method is called with the input integers a and b.
  d) The result (the swapped values) is printed for each test case.
