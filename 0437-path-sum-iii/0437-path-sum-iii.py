# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        from collections import defaultdict

        prefix=defaultdict(int)
        prefix[0]=1
        count=0

        def dfs(node, curr_sum):
            nonlocal count
            if not node:
                return
            curr_sum += node.val
            count += prefix[curr_sum - targetSum]

            prefix[curr_sum] += 1

            dfs(node.left, curr_sum)
            dfs(node.right, curr_sum)
            prefix[curr_sum] -= 1
        dfs(root,0)
        return count
        