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
# 3rd
https://github.com/colorbox/leetcode/pull/13/files#diff-d9587deaaf609e492fff8cf22814dcb335b1d72972e3dc6b026eecce5aca3d0c
を参考に再構築
結果：実行時間44ms　（2ndは39ms・・・なぜだろう）

小田さんコメント：
isBalanced と height をペアにして返すようにすると、メモをしない再帰でも O(n) になります。
キャッシュするのも一つですが。
これ、友達を木の上の各ノードに立たせてですよ。電話させるんですよ。
で、マニュアルをばらまきます
「木の高さいくら?」と聞かれた場合は、電話を保留状態にし、自分が null でない場合、部下全員に「木の高さいくら?」と電話をかけて、大きい方の数字に1を足してください。自分が null の場合は0です。保留を解除して返事をして下さい。
「バランスしている?」と聞かれた場合は、電話を保留状態にして、部下全員に「木の高さいくら?」と聞いて下さい。返事が返ってきたら、今度は部下全員に「バランスしている?」と聞いて下さい。
電話は、一回で済ませて下さい。isBalanced と height をペアにして返すようにすると、メモをしない再帰でも O(n) になります。

``` Python
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.GetHeight(root) != -1
    def GetHeight(self, root):
        if not root: return 0

        leftheight = self.GetHeight(root.left)
        if leftheight == -1: return -1

        rightheight = self.GetHeight(root.right)
        if rightheight == -1: return -1

        if abs(leftheight - rightheight) >= 2:
            return -1
        
        return max(leftheight, rightheight) + 1
```


# 4th
おそらく，isBalancedとGetHeightが並列でいるのが遅い原因かと仮説をたてて
２つを統合するという方針に変更
（実行時間が短いコードを参考にしました）
結果：33ms



``` Python
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
```

# 5th
GetHeightのネーミングを変更
isbalancedの要素を追加

``` Python
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def GetHeight_and_isBalanced(node):
            # check if base root or not
            if not node: return 0, True

            # check height and isBalanced
            left_height, i_leftBalanced = GetHeight_and_isBalanced(node.left)
            right_height, i_rightBalanced = GetHeight_and_isBalanced(node.right)

            # calculate current node height
            current_height = max(left_height, right_height) + 1

            # check if current node is balanced or not
            i_Balanced = i_leftBalanced and i_rightBalanced and (abs(left_height - right_height) <=1)

            return current_height, i_Balanced
        _, i_Balanced = GetHeight_and_isBalanced(root)
        return i_Balanced
```
