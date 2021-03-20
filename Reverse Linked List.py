'''
Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head == None or head.next == None:  # Size 1 or 2
            return head
        else:                                   # Size >= 2
            lyst = []
            probe = head
            while probe!= None:
                lyst.append (probe.val)
                probe = probe.next
                
            head = ListNode (lyst[len(lyst)-1])
            probe = head
            for item in lyst [len(lyst)-2::-1]:
                node = ListNode (item, None)
                probe.next = node
                probe = probe.next
                
            return (head)