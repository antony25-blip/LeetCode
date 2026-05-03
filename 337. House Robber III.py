# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def valid(TreeNode):
            if TreeNode == None:
                return(0,0)
            left_choice = valid(TreeNode.left)
            right_choice = valid(TreeNode.right)
            rob=TreeNode.val + left_choice[1] + right_choice[1]
            skip=max(left_choice[0],left_choice[1])+max(right_choice[0],right_choice[1])
            return(rob,skip)
        val=valid(root)
        return max(val)
        
