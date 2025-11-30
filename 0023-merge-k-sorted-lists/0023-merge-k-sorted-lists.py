# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(l1,l2):
            temp=ListNode(0)
            curr=temp
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next=l1
                    l1=l1.next
                else:
                    curr.next=l2
                    l2=l2.next
                curr=curr.next
            curr.next=l1 or l2
            return temp.next
        if not lists:
            return None
        res=None
        for lst in lists:
            res=merge(res,lst)
        return res
        
        