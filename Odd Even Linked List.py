'''
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]
Example 2:


Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
 

Constraints:

The number of nodes in the linked list is in the range [0, 104].
-106 <= Node.val <= 106
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head == None or head.next == None:
            return head
        
        odd_prehead = ListNode (0, None)
        even_prehead = ListNode (0, None)
        even = even_prehead
        odd = odd_prehead
        probe = head
       
        index = 1
        while probe!= None:
            if index%2 == 1:
                odd.next = probe
                odd = odd.next
            else:
                even.next = probe
                even = even.next
            probe = probe.next
            index = index + 1
        even.next = None
        odd.next = even_prehead.next
        return odd_prehead.next