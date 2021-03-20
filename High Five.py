'''
Given a list of the scores of different students, items, where items[i] = [IDi, scorei] represents one score from a student with IDi, calculate each student's top five average.

Return the answer as an array of pairs result, where result[j] = [IDj, topFiveAveragej] represents the student with IDj and their top five average. Sort result by IDj in increasing order.

A student's top five average is calculated by taking the sum of their top five scores and dividing it by 5 using integer division.

 

Example 1:

Input: items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
Output: [[1,87],[2,88]]
Explanation: 
The student with ID = 1 got scores 91, 92, 60, 65, 87, and 100. Their top five average is (100 + 92 + 91 + 87 + 65) / 5 = 87.
The student with ID = 2 got scores 93, 97, 77, 100, and 76. Their top five average is (100 + 97 + 93 + 77 + 76) / 5 = 88.6, but with integer division their average converts to 88.
Example 2:

Input: items = [[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100]]
Output: [[1,100],[7,100]]
 

Constraints:

1 <= items.length <= 1000
items[i].length == 2
1 <= IDi <= 1000
0 <= scorei <= 100
For each IDi, there will be at least five scores.
'''

class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        I = Solution ()
        ID_list = []
        for item in items:
            ID = item[0]
            if ID not in ID_list:
                ID_list.append(ID) 
                
        dyct = {}
        for ID in ID_list:
            dyct[ID] = []
            
        for item in items:
            ID = item[0]
            score = item[1]
            dyct[ID].append(score)
            
        output = []
        for ID in dyct:
            output.append([ID,I.top_five_average(dyct[ID])])
            
        return (output)
    
    def top_five_average(self,lyst):
        score1 = max(lyst)
        lyst.remove(score1)
        score2 = max(lyst)
        lyst.remove(score2)
        score3 = max(lyst)
        lyst.remove(score3)
        score4 = max(lyst)
        lyst.remove(score4)
        score5 = max(lyst)
       
        return (score1+score2+score3+score4+score5)//5