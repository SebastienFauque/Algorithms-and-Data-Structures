from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1
        else:
            head = None
            current = None
            while list1 is not None or list2 is not None:
                head, current, list1, list2 = update_lists(
                    head, current, list1, list2)

        return head


def update_lists(head, merged, l1, l2):
    l1_val = l1.val if l1 else float('inf')
    l2_val = l2.val if l2 else float('inf')

    if l1_val <= l2_val:
        if head is None:
            merged = ListNode(l1.val)
            head = merged
        else:
            merged.next = ListNode(l1.val)
            merged = merged.next

        l1 = l1.next

    elif l2_val < l1_val:
        if head is None:
            merged = ListNode(l2.val)
            head = merged
        else:
            merged.next = ListNode(l2.val)
            merged = merged.next

        l2 = l2.next

    return (head, merged, l1, l2)


l1 = [1, 2, 4]
l2 = [1, 3, 4]
h1 = None
h2 = None
ll1 = None
ll2 = None

ls = zip(l1, l2)
for i, (n1, n2) in enumerate(ls):
    if i == 0:
        h1 = ListNode(n1)
        h2 = ListNode(n2)
        ll1 = h1
        ll2 = h2
    else:
        ll1.next = ListNode(n1)
        ll2.next = ListNode(n2)
        ll1 = ll1.next
        ll2 = ll2.next

test = Solution()
res = test.mergeTwoLists(h1, h2)

# Expected ll output: [1,1,2,3,4,4]
while res:
    print(res.val)
    res = res.next
