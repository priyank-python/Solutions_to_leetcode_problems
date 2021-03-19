'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
 

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
'''

import itertools
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        telemap = {'2':['a','b','c'],
            '3':['d','e','f'], '4':['g','h','i'], '5':['j','k','l'], '6':['m','n','o'],
            '7':['p','q','r','s'], '8':['t','u','v'], '9':['w','x','y','z']}
        
        
        pullouts = []
        
        for ch in digits:
            pullouts.append(telemap.get(ch))
            
        # solution1 = list(itertools.combinations (pullouts, len(pullouts)))
        
        solution2 = []
        solution3 = []
        solution4 = []
        
        
             
        if len(pullouts) == 0:
            return ([])
        else:
            if len(pullouts) == 1:
                return (pullouts[0])
            else:
                for x in (pullouts[0]):
                    for y in (pullouts[1]):
                        mystr = x + y
                        solution2.append(mystr)
                if len(pullouts) == 2:
                    return (solution2)
                else:
                    for z in (solution2):
                        
                        for w in (pullouts[2]):
                            mystr = z+w
                            solution3.append(mystr)
                    if (len(pullouts)) == 3:
                        return (solution3)
                    else:
                        for q in (solution3):
                            
                            for r in (pullouts[3]):
                                mystr = q+r
                                solution4.append(mystr)
                        return (solution4)
                        