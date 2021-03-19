'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
Example 4:

Input: x = 0
Output: 0
 

Constraints:

-231 <= x <= 231 - 1
'''

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        if x>=0:
            sign = 'positive'
        else:
            sign = 'negative'
            x = -1 * x
            
        
        r = 0
        while x!=0:
            d = x%10
            r = r*10 + d
            x = x//10
        if sign == 'positive':
            solution = r
        else:
            solution = -1*r
        
        if solution >= (-1*(2**31)) and solution <= ((2**31)-1):
            return (solution)
        else:
            return 0