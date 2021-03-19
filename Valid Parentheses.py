'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = []
        
        
        
        for ch in s:
            if len(stack) == 0:
                if ch == ')' or ch == ']' or ch == '}':
                    return False
             
            if ch =='(' or ch == '[' or ch == '{':
                stack.append (ch) # The append method serves as push 
            else:
                try:
                    if ch == ')':
                        if stack[len(stack)-1] == '(':
                            stack = stack[0:len(stack)-1] # This statement serves as pop
                        else:
                            return False
                    
                    if ch == ']':
                        if stack[len(stack)-1] == '[':
                            stack = stack[0:len(stack)-1]
                        else:
                            return False
                    
                    if ch == '}':
                        if stack[len(stack)-1] == '{':
                            stack = stack[0:len(stack)-1]
                        else:
                            return False
                except:
                    stack = []
                    
        if len(stack) == 0:
            return True
        else:
            return False