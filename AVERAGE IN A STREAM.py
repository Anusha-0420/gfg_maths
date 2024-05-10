Given a stream of incoming numbers, find average or mean of the stream at every point.
  code:

class Solution:
	def streamAvg(self, arr, n):
		add=0
		l=[]
		for i in range(1,n+1):
		    add += arr[i-1]
		    avg = float(add/i)
		    l.append(avg)
	    return l

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.streamAvg(arr, n)
        for x in ans:
            print('%.2f'%x, end=" ")
        print()
        tc -= 1
Explanation:
1. The Solution class is defined, which presumably contains methods for solving specific problems.
2. The streamAvg method takes three arguments: self (indicating that this method is part of a class), a list of integers arr, and an integer n.
3. It initializes the variable add to 0 and an empty list l.
4. The code iterates through the numbers from 1 to n (inclusive) using range(1, n + 1).
5. For each number i, it adds the i-th element of the arr list to add.
6. It calculates the average by dividing add by i and stores it in the variable avg.
7. The average value is appended to the list l.
8. The method returns the list l.
9. The code reads an integer tc (presumably the number of test cases) and iterates through each test case:
  a) For each test case, it reads an integer n.
  b) It reads a list of integers arr.
  c) An instance of the Solution class is created.
  d) The streamAvg method is called with the input list arr and integer n.
  e) The resulting list of average values is printed, with each value formatted to two decimal places.
However, there are a few things to note:

The code assumes that the input format is as described (number of test cases followed by the integer values and the list of integers).
It does not handle invalid inputs or edge cases.

