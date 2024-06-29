# 2-05_ReverseLinkedList
Author: WaveAlchemist
URL: https://leetcode.com/problems/reverse-linked-list/description/
Given the head of a singly linked list, reverse the list, and return the reversed list.
Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

# 1st-3rd
1st時点では最後までノードを進めてそこから順番を入れ替えるという考え方をしたが，コードには落とせなかった．
2ndでは以下を参照し，3rd時点で1－2分で実装できるようになった
https://leetcode.com/problems/reverse-linked-list/solutions/4907312/very-easy-python3-solution/

``` Python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # initialize current, previous, and front node
        curr = head
        prev = None
        front = None
        # reverse listnode until curr does not reach the end
        while curr:
            front = curr.next # renew front node
            curr.next = prev  # reverse current node
            prev = curr       # renew previous node
            curr = front      # proceed current node at front node
        return prev
```
# 4th
discord上の議論を見て，再帰でも実装できないかに挑戦
https://discordapp.com/channels/1084280443945353267/1231966485610758196/1239417493211320382

``` Python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverseListHelper(rev, curr):
            if not curr:
                return rev
            front = curr.next
            curr.next = rev
            return reverseListHelper(curr, front)
        return reverseListHelper(None, head)
```

# 5th
discord上の議論を見て再度整理
https://github.com/ryoooooory/LeetCode/pull/14
⇒currよりはnode??

odaさんコメント：
ループは仕事の引き継ぎだと思うといいんじゃないでしょうか。

「直径 1 m 金属の輪っか」に 2 m の鎖が生えていてその先に「南京錠」がついているとしましょう。LinkedList とは、これを一直線に並べて、南京錠を隣の輪っかにつなげていったものです。最後の南京錠は何にもつながっていません。

この南京錠の鎖が1万個あるので、一日1000個ずつ担当を決めてひっくり返していきます。あなたはこの職場に3日目に来ました。何が引き継ぎされていなかったら怒り出しますか。

kitakenコメント：
未処理のlistnode⇒rev(reverseの意味), 処理済みのlistnode⇒node

``` Python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        prev = None
        front = None
        while node:
            front = node.next
            node.next = prev
            prev = node
            node = front
        return prev
```

``` Python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverseListHelper(rev, node):
            if not node:
                return rev
            front = node.next
            node.next = rev
            return reverseListHelper(node, front)
        return reverseListHelper(None, head)
```

