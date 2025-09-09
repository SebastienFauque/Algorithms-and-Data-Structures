# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        res = None

        while head:
            resHead = ListNode(val=head.val)
            resHead.next = res
            res = resHead

            if head.next:
                head = head.next
            else:
                break

        return res