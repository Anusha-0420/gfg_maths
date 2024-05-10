Given the first 2 terms a1 and a2 of an Arithmetic Series.Find the nth term of the series. 
Code:
class Solution:
    def nthTermOfAP(self, a1 : int, a2 : int, n : int) -> int:
        # code here
        d = a2-a1
        n_term = a1+(n-1)*d
        return n_term
        
if __name__=="__main__":
    t = int(input())
    for _ in range(t):     
        a1 = int(input())
        a2 = int(input())
        n = int(input())
        obj = Solution()
        res = obj.nthTermOfAP(a1, a2, n)        
        print(res)
Explanation:
1. The Solution class is defined, which presumably contains methods for solving specific problems.
2. The nthTermOfAP method takes four arguments: self (indicating that this method is part of a class), and three integers: a1, a2, and n.
3. It calculates the common difference d between consecutive terms in the arithmetic progression (AP) using d = a2 - a1.
4. It computes the n-th term of the AP using the formula: n_term = a1 + (n - 1) * d.
5. The method returns the n-th term.
6. The code reads an integer t (presumably the number of test cases) and iterates through each test case:
  a) For each test case, it reads three integers: a1, a2, and n.
  b) An instance of the Solution class is created.
  c) The nthTermOfAP method is called with the input integers a1, a2, and n.
  d) The result (the n-th term of the AP) is printed for each test case.
