'''
Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.

 

Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: ["cool","lock","cook"]
Output: ["c","o"]
 

Note:

1 <= A.length <= 100
1 <= A[i].length <= 100
A[i][j] is a lowercase letter
'''

class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        
        output = []
        
        characters = []
        for ch in A[0]:
            characters.append (ch)
            
        for ch in characters:
            common = True
            for word in A:
                if ch not in word:
                    common = False
                    break
            if common == True:
                output.append (ch)
                B = []
                for word in A:
                    B.append (word.replace(ch,'',1))
                A = B
                    
        return (output)