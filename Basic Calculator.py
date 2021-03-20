'''
Given a string s representing an expression, implement a basic calculator to evaluate it.

 

Example 1:

Input: s = "1 + 1"
Output: 2
Example 2:

Input: s = " 2-1 + 2 "
Output: 3
Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
 

Constraints:

1 <= s.length <= 3 * 105
s consists of digits, '+', '-', '(', ')', and ' '.
s represents a valid expression.
'''

class Solution(object):
    def calculate(self, s):
        I = Solution()
        s = s.replace(' ','')
        if ')' in s:
            index2 = s.find(')')
            index = index2
            while True:   
                if s[index] == '(':
                    index1 = index
                    break
                index = index - 1
            return (I.calculate(s[0:index1]+str(I.evaluation(s[index1+1:index2]))+s[index2+1:] ))
        else:
            return ((I.evaluation(s)))
        
    def evaluation (self, expression):
        expression = expression.replace('--','+') + ' '
        
        result = 0
        num = 0
        sign = 'plus'
        for ch in expression:
            if ch.isdigit():
                num = num*10 + int(ch)
            else: 
                
                if sign == 'plus':
                    result = result + int(num)
                else:
                    result = result - int(num)
                num = 0
            
                if ch == '+':
                    sign = "plus"
                elif ch == '-':
                    sign = 'minus'
            
        return (result)