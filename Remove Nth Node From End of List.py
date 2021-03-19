'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Follow up: Could you do this in one pass?

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
Accepted
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        node = head
        size = 0
        while node != None:
            size = size + 1
            node = node.next
            
        if size == 1 and n == 1:
            head = None
            return (head)
       
        if n == 1:  # Get to the second last item and set it's next attribute to None
            probe = head
            index = 0
            while index < (size-n-1):
                probe = probe.next
                index = index + 1
            probe.next = None
        else:
            probe = head
            index = 0
            while index < (size-n):
                probe = probe.next
                index = index + 1
            probe.val = probe.next.val
            if n == 2:
                probe.next = None
            else:
                probe.next = probe.next.next
                
        return head
            