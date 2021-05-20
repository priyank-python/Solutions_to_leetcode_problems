'''
Given the head of a linked list, return the list after sorting it in ascending order.

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

 

Example 1:


Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:


Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is in the range [0, 5 * 104].
-105 <= Node.val <= 105
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        probe = head
        lyst = []
        while probe != None:
            lyst.append(probe.val)
            probe = probe.next
        lyst.sort ()
        if len(lyst) <= 1:
            return head
        else:
            first_node = ListNode(lyst[0],None)
            probe = first_node
            for value in lyst[1:]:
                node = ListNode(value,None)
                probe.next = node
                probe = probe.next
            return (first_node)
        '''
        Time Complexity = O(n)
        Space Complexity = O(n)
        '''