# 06_InvertBinaryTree
Author: WaveAlchemist  
URL: https://leetcode.com/problems/invert-binary-tree/

# 1st
方針：
Treeがn層あるとして，以下のようなアルゴリズムを考案
1) n層目のTreeNodeの値の左右を入れ替える
2) n-i層目のTreeNodeの値の左右を入れ替える (i=1~n-1)
TreeNodeの形式が理解できず，コードには書けなかった．
⇒解答例を確認
https://leetcode.com/problems/invert-binary-tree/solutions/3199238/0-ms-simplest-solution-full-explanation-c-python3/

# 2nd 
解答例を読み再度自分で構築

``` Python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # check if root is base or not
        if not root:
            return root
        # invert left and right lower trees
        self.invertTree(root.left)
        self.invertTree(root.right)
        # invert left and right elements
        root.left, root.right = root.right, root.left
        # return inverted tree
        return root
```
