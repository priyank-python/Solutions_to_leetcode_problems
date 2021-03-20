'''
Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

 

Example 1:

Input: s = "3+2*2"
Output: 7
Example 2:

Input: s = " 3/2 "
Output: 1
Example 3:

Input: s = " 3+5 / 2 "
Output: 5
 

Constraints:

1 <= s.length <= 3 * 105
s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
s represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, 231 - 1].
The answer is guaranteed to fit in a 32-bit integer.
'''


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # Remove all spaces from the expression
        
        s = s.replace (' ','')
        
        # Derive a list (sequence) of operands and operators from the expression
        
        lyst = []
        operand = ''
        for ch in s:
            if ch.isdigit ():
                operand = operand + ch
            else:
                lyst.append (operand)
                operand = ''
                lyst.append (ch) # The operator
        lyst.append (operand)
        
        # Convert the list (representing an infix expression) to postfix form
        
        p = [] # post-fix expression
        stack = [] # stack of operators
        operator_precedence = {'*' : 2, '/' : 2,'+' : 1, '-' : 1}

        for token in lyst:
            if token.isdigit ():
                p.append (token) #operand
            else:
                stack.append (token) # operator
                for index in range (len(stack)-2,-1,-1):
                    if operator_precedence.get(stack[index])>=operator_precedence.get (token):
                        p.append (stack[index])
                        stack [index] = token
                        stack = stack [0:len(stack)-1]
       
        for index in range (len(stack)-1,-1,-1):
            p.append (stack [index])
                        
                
        # Evaluate the postfix expression
        
        I = Solution ()
        
        stack = []
        
        for token in p:
            if token.isdigit ():
                stack.append (token)
            else:
                value = I.evaluate (int(stack[len(stack)-2]),int (stack[len(stack)-1]), token)
                stack = stack [0:len(stack)-2]
                stack.append (str(value))
        return (stack[0])
    
    def evaluate (self, m, n, o):
        if o == '+':
            return (m+n)
        elif o == '-':
            return (m-n)
        elif o == '*':
            return (m*n)
        else:
            return (m/n)