# 11_BalancedBinaryTree
Author: WaveAlchemist  
URL:https://leetcode.com/problems/balanced-binary-tree/

# 1st
再帰関数の利用を考え，Treeの左，右の総数itl, itrを繰りかえし足し算し
最終的にitlとitrの差が1以内ならheight-balancedと判定する
という方針を考えたが，コードには書き起こせなかった
``` Python
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # check if empty tree or not
        if not root:
            return True
        # add counter 
        itl = 0
        itr = 0
        if root.left:
            itl += 1
            self.isBalanced(root.left)
        if root.right:
            itr += 1
            self.isBalanced(root.right)
        if abs(itl-itr) <= 1:
            return True
        else:
            return False
```

# 2nd
https://leetcode.com/problems/balanced-binary-tree/solutions/2428871/very-easy-100-fully-explained-c-java-python-javascript-python3/
を参照
何も見ずに5分で構築できるようにはしましたが，
理解をさらに深めたいところです

``` Python
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.Height(root) >= 0 
    def Height(self, root):
        # Base case
        if not root: return 0
        # Height of left and right subtrees
        leftheight, rightheight = self.Height(root.left), self.Height(root.right)
        # If diff of height of left and right subtree >= 2 -> return -1
        if leftheight == -1 or rightheight == -1 or abs(leftheight-rightheight) >= 2:
            return -1
        # Return height of tree
        return max(leftheight, rightheight) + 1 
```



