'''
Given the head of a linked list, rotate the list to the right by k places.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]
 

Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        length = 0
        probe = head
        while probe != None:
            length = length + 1
            probe = probe.next
            
        if length<=1 or k == 0:
            return head
        else:
            k = k-int (length*math.floor(k/length))
            if k == length or k == 0:
                return head
            else:
                probe = head
                for count in range (0,length-k-1):
                    probe = probe.next
                prehead = ListNode (-1,probe.next)
                probe.next = None
                newprobe = prehead.next
                while newprobe.next != None:
                    newprobe = newprobe.next
                newprobe.next = head
                return (prehead.next)