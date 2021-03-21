'''
Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character.

Return the power of the string.

 

Example 1:

Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.
Example 2:

Input: s = "abbcccddddeeeeedcba"
Output: 5
Explanation: The substring "eeeee" is of length 5 with the character 'e' only.
Example 3:

Input: s = "triplepillooooow"
Output: 5
Example 4:

Input: s = "hooraaaaaaaaaaay"
Output: 11
Example 5:

Input: s = "tourist"
Output: 1
 

Constraints:

1 <= s.length <= 500
s contains only lowercase English letters.
'''

class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        ch_set = set ()
        for ch in s:
            ch_set.add(ch)
        if len (ch_set) == 1:
            return len(s)
        else:
            s = s + ' '
            ch1 = s[0]
            c = 0
            C = []
            for ch2 in s[1:]:
                if ch2 == ch1:
                    c = c + 1
                else:
                    ch1 = ch2
                    C.append(c)
                    c = 1
            return (max(C))