For a given 3 digit number, find whether it is armstrong number or not. 

Code:
class Solution:
    def armstrongNumber (self, n):
        n = str(n)
        l = len(n)
        add = 0
        for i in n:
            add += (int(i))**(l)
        if add == int(n):
            return "Yes"
        else:
            return "No"
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = input()
        n=int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))
Explaination :

1. The Solution class is defined, which presumably contains methods for solving specific problems.
2. The armstrongNumber method takes two arguments: self (indicating that this method is part of a class) and an integer n.
3. It converts the integer n to a string to calculate its length.
4. The variable l stores the length of the string representation of n.
5. It initializes the variable add to 0.
6. The code iterates through each character in the string representation of n.
7. For each character, it raises the integer value of that character to the power of l and adds it to add.
8. If the sum of these powered values equals the original integer n, it returns “Yes” (indicating that n is an Armstrong number).
9. Otherwise, it returns “No”.
10. The code reads an integer t (presumably the number of test cases) and iterates through each test case.
11. For each test case, it reads an integer n.
12. An instance of the Solution class is created, and the armstrongNumber method is called with the input integer n.
13. The result (either “Yes” or “No”) is printed for each test case.
