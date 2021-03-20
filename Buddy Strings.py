'''
Given two strings a and b, return true if you can swap two letters in a so the result is equal to b, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at a[i] and b[j]. For example, swapping at indices 0 and 2 in "abcd" results in "cbad".

 

Example 1:

Input: a = "ab", b = "ba"
Output: true
Explanation: You can swap a[0] = 'a' and a[1] = 'b' to get "ba", which is equal to b.
Example 2:

Input: a = "ab", b = "ab"
Output: false
Explanation: The only letters you can swap are a[0] = 'a' and a[1] = 'b', which results in "ba" != b.
Example 3:

Input: a = "aa", b = "aa"
Output: true
Explanation: You can swap a[0] = 'a' and a[1] = 'a' to get "aa", which is equal to b.
Example 4:

Input: a = "aaaaaaabc", b = "aaaaaaacb"
Output: true
 

Constraints:

1 <= a.length, b.length <= 2 * 104
a and b consist of lowercase letters.
'''

class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        
        if len(A) != len (B):
            return False
        elif A == B:
            swappable = False
            for ch in A:
                if A.count(ch) >= 2:
                    swappable = True
            return swappable
        else:
            loci_of_difference = []
            index = 0
            while index < len(A):
                if A[index] != B[index]:
                    loci_of_difference.append(index)
                index = index + 1
            if len (loci_of_difference) != 2:
                return False
            else:
                index1, index2 = loci_of_difference[0], loci_of_difference[1]
                if A[index1] == B[index2] and A[index2] == B[index1]:
                    return True
                else:
                    return False
        