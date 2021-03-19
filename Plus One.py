'''
Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

 

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Example 3:

Input: digits = [0]
Output: [1]
 

Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9
'''

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        integer = 0
        for x in digits:
            d = int(x)
            integer = integer*10+d
        
        integer = integer + 1
        output = []
        
        while integer!=0:
            d = integer%10
            output.append(str(d))
            integer = integer//10
        
        
        
        if len(output)<len(digits):
            difference = len(digits) - len(output)
            for x in range(0,difference):
                output.append('0')
                
        output.reverse()
        
        return (output)
        