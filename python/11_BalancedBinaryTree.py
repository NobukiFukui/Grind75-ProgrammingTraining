# ===============================================================
# (program) 11_BalancedBinaryTree
# WaveAlchemist
# Description: Given a binary tree, determine if it is height-balanced
#
# URL: https://leetcode.com/problems/balanced-binary-tree/description/
# ===============================================================

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def GetHeight(node):
            # check if base root or not
            if not node: return 0, True

            # check height and isBalanced
            left_height, i_leftBalanced = GetHeight(node.left)
            right_height, i_rightBalanced = GetHeight(node.right)

            # calculate current node height
            current_height = max(left_height, right_height) + 1

            # check if current node is balanced or not
            i_Balanced = i_leftBalanced and i_rightBalanced and (abs(left_height - right_height) <=1)

            return current_height, i_Balanced
        _, i_Balanced = GetHeight(root)
        return i_Balanced

