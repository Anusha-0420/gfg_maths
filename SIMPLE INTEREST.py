Given three integers P,R and T, denoting Principal, Rate of Interest and Time period respectively.Compute the simple Interest.
  Code:

class Solution:
    def simpleInterest(self,A,B,C):
        #code here
        si = (B/100)*A*C
        return si

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        P,R,T=map(int,input().strip().split(' '))
        ob=Solution()
        print('%.2f'%ob.simpleInterest(P,R,T))
Explanation: 
1. The Solution class contains a method called simpleInterest.
2. Given the principal amount P, rate of interest R, and time T, it calculates the simple interest using the formula:
                 Simple Interest= P⋅R⋅T​/100
3. The code reads an integer t (number of test cases) and iterates through each test case:
  a) For each test case, it reads three integers: P, R, and T.
  b) An instance of the Solution class is created.
  c) The simpleInterest method is called with the input values.
  d) The result (simple interest) is printed with 2 decimal places.

Note:

The code assumes that the input format is as described (number of test cases followed by the integer values).
It does not handle invalid inputs or edge cases.

