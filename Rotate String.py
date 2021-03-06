'''
We are given two strings, A and B.

A shift on A consists of taking string A and moving the leftmost character to the rightmost position. For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True if and only if A can become B after some number of shifts on A.

Example 1:
Input: A = 'abcde', B = 'cdeab'
Output: true

Example 2:
Input: A = 'abcde', B = 'abced'
Output: false
Note:

A and B will have length at most 100.
'''

class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        
        if len(A) != len (B):
            return False
        elif A == '' or B == '':
            return True
        elif len (A) == 1:
            if A == B:
                return True
        else:
            result = True
            iterations = 0
            A = A[1:] + A[0]
            while iterations <= len(A):
                if A == B:
                    return True
                    break
                A = A[1:] + A[0]
                iterations = iterations + 1
            if A == B:
                return True
            else:
                return False