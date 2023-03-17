# LeetCode 21
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
  def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    # Create a listNode to store the merged list
    merged = ListNode()
    # Assign the merged list to be the current pointer
    current = merged

    # While list1 and list2 exist:
    while list1 and list2:
      if list1.val < list2.val:
        current.next = list1
        list1 = list1.next
      else:
        current.next = list2
        list2 = list2.next

      # Move current to the recently placed value
      current = current.next

    # Once one of the lists is exhausted, place in
    # the rest of the remaining otherlist
    if list1:
      current.next = list1
    else list2:
      current.next = list2

    # Return the head of the merged list.
    return merged.next