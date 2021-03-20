'''
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
 

Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
'''

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        '''
        The problem description should also mention that the same character cannot map onto 
        two different characters.
        That is, it is one-to-one mapping.
        '''
        
        dyct = {}
        
        for index in range (len(s)):
            if s[index] not in dyct:
                if t[index] not in dyct.values(): 
                    dyct[s[index]] = t[index]
                else:
                    return False
            else:
                if t[index] != dyct.get(s[index]):
                    return False
        
        return True
        