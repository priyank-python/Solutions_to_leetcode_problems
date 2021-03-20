'''
Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.

 

Example 1:

Input: date = "2019-01-09"
Output: 9
Explanation: Given date is the 9th day of the year in 2019.
Example 2:

Input: date = "2019-02-10"
Output: 41
Example 3:

Input: date = "2003-03-01"
Output: 60
Example 4:

Input: date = "2004-03-01"
Output: 61
 

Constraints:

date.length == 10
date[4] == date[7] == '-', and all other date[i]'s are digits
date represents a calendar date between Jan 1st, 1900 and Dec 31, 2019.
'''



class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        
        year = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        leap_year = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            
        day = 0
        
        month = int(date[5:7])
        
        for x in range (1,month):
            if int(date[0:4]) % 4 == 0 and int(date[0:4]) % 100 != 0:
                day = day + leap_year [x]
            else:
                day = day + year [x]
                
        day = day + int(date[8:])
        
        return day