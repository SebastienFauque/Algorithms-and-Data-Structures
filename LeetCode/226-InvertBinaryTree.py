# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.recurse(root)
        
    
    def recurse(self, subroot):
        if hasattr(subroot, 'left') and hasattr(subroot, 'right'):
            temp = subroot.left
            subroot.left = subroot.right
            subroot.right = temp
            self.recurse(subroot.left)
            self.recurse(subroot.right)
        elif hasattr(subroot, 'left'):
            subroot.right = subroot.left
            subroot.left = None
            self.recurse(subroot.right)
        elif hasattr(subroot, 'right'):
            subroot.left = subroot.right
            subroot.right = None
            self.recurse(subroot.left)

        return subroot
        