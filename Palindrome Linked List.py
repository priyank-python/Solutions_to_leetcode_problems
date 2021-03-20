'''
iven the head of a singly linked list, return true if it is a palindrome.

 

Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false
 

Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        values = []
        probe = head
        while probe!= None:
            values.append (probe.val)
            probe = probe.next
            
        if len(values) <= 1:
            return True
        else:
            index1 = 0
            index2 = len(values)-1
            while index1 <= index2:
                if values[index1] != values[index2]:
                    return False
                index1 = index1 + 1
                index2 = index2 - 1
            return True