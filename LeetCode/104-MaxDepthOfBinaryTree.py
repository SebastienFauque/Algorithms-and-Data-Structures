# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dive(root, 0)

    def dive(self, subroot, currentDepth: int):
        if not subroot: return currentDepth

        d1 = self.dive(subroot.left, currentDepth+1)
        d2 = self.dive(subroot.right, currentDepth+1)

        return max(d1, d2)