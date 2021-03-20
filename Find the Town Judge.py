'''
In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

 

Example 1:

Input: N = 2, trust = [[1,2]]
Output: 2
Example 2:

Input: N = 3, trust = [[1,3],[2,3]]
Output: 3
Example 3:

Input: N = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
Example 4:

Input: N = 3, trust = [[1,2],[2,3]]
Output: -1
Example 5:

Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3
 

Constraints:

1 <= N <= 1000
0 <= trust.length <= 10^4
trust[i].length == 2
trust[i] are all different
trust[i][0] != trust[i][1]
1 <= trust[i][0], trust[i][1] <= N
'''

class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        
        '''
        If a town judge exists, he must appear at second index paired with every other person.
        Secondly, he must not be present at first index in any pair.
        Let us check the second condition first. And then the first condition.
        '''
        
        suspects = []
        
        for person in range (1,N+1):
            present = False
            for trust_pair in trust:
                if person == trust_pair [0]:
                    present = True
                    break
            if present == False:
                suspects.append(person)
                
        if len(suspects) == 0:
            return (-1)
        else:
            for suspect in suspects:
                trusted_by = []
                for trust_pair in trust:
                    if trust_pair[1] == suspect:
                        trusted_by.append (trust_pair[0])
                if len(trusted_by) == N-1:
                    return suspect
        return (-1)
                