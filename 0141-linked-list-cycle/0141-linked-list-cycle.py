# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        ptr1 = head
        ptr2 = head

        while ptr2 and ptr2.next:
            ptr1 = ptr1.next
            ptr2 = ptr2.next.next

            # Cycle
            if ptr1 == ptr2:
                return True
        # no cycle
        return False

        