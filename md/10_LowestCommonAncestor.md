# 10_LowestCommonAncestor
Author: WaveAlchemist  
URL: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/

# 1st
方針：
最小共通祖先の探索をするので，
元のTreeNodeから順番に下層に移動していき，
p及びqと共通になる時点でstopし，そのTreeNodeを返す
結果：
失敗

``` Python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == p or root == q:
            return root.val
        if not root.left: 
            self.lowestCommonAncestor(root.left, p, q)
        if not root.right:
            self.lowestCommonAncestor(root.right, p, q)
```

# 2nd
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/solutions/1347857/c-java-python-iterate-in-bst-picture-explain-time-o-h-space-o-1/
を参照して，再構築した
p.val及びq.valの大小large, smallを決めてroot.valがそれらのうちどこに属するか
・root.val > large　⇒　左側の木にある
・root.val < small　⇒　右側の木にある
・small <= root.val <= large ⇒ rootそのものがLCA

``` Python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # decide large or small value of trees
        small = min(p.val, q.val)
        large = max(p.val, q.val)
        # repeat 
        while root:
            if root.val > large:   # p and q belong to the left subtree
                root = root.left
            elif root.val < small: # p and q belong to the right subtree
                root = root.right
            else:                  # root is the LCA b/w p and q
                return root
        return None                # no LCA is detected
```

# 3rd
2ndのコードをさらに簡潔に書けないかを検討した．
whileループの部分をself.で再帰関数とした．

``` Python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
```
