'''
Given an integer n, return true if and only if it is an Armstrong number.

The k-digit number n is an Armstrong number if and only if the kth power of each digit sums to n.

 

Example 1:

Input: n = 153
Output: true
Explanation: 153 is a 3-digit number, and 153 = 13 + 53 + 33.
Example 2:

Input: n = 123
Output: false
Explanation: 123 is a 3-digit number, and 123 != 13 + 23 + 33 = 36.
 

Constraints:

1 <= n <= 108
'''


import math
class Solution(object):
    def isArmstrong(self, N):
        """
        :type N: int
        :rtype: bool
        """
        n=N
        m=N
        
        k=0
        while N!=0:
            k = k + 1
            N = N//10
            
        sum = 0
        while n!=0:
            d=n%10
            sum = sum + math.pow(d,k)
            n=n//10
        
        if sum == m:
            return True
        else:
            return False
        