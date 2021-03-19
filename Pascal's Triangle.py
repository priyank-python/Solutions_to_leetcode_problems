'''
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 

Constraints:

1 <= numRows <= 30
'''

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        if numRows == 0:
            return []
        lyst = [[]*numRows]
        lyst[0] = [1]
        last_row = lyst[0]
        for length in range (2,numRows+1):
            next_row = [0]*length
            next_row[0]=1
            for index in range (1,length-1):
                next_row[index] = last_row[index-1] + last_row[index]
            next_row[length-1]=1
            lyst.append(next_row)
            last_row = next_row
        
        return (lyst)