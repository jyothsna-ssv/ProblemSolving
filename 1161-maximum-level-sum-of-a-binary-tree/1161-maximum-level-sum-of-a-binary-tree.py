# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q=deque([root])
        max_sum=-10**20
        level=best=1

        while q:
            curr_sum=0
            for  _ in range(len(q)):
                n=q.popleft()
                curr_sum += n.val
                if n.left:q.append(n.left)
                if n.right: q.append(n.right)
            if curr_sum > max_sum:
                max_sum = curr_sum
                best=level
            level += 1
        return best
        
        