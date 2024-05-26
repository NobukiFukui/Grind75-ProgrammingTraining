# 12_LinkedListCycle
Author: WaveAlchemist  
URL:https://leetcode.com/problems/linked-list-cycle

# 1st 
問題文の理解に時間がかかるものの，
１飛びおよび２飛びのポインタを用意し，それらが等しくなればcycleがあるという判定
実行時間：48ms, メモリ：19.03MB

``` Python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # check if head is null -> no cycle
        if not head: return False
        # get slow and fast pointers 
        slow = head
        fast = head.next
        # while loop
        while slow != fast:
            # check if fast pointer is end
            if not fast or not fast.next: return False
            slow = slow.next      # proceed one node
            fast = fast.next.next # proceed two nodes
        return True
```

# 2nd
PEP8に基づいてマイナーチェンジ

``` Python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # check if head is null -> false (no cycle)
        if not head:
            return False
        # set pointer nodes, slow and fast
        # slow checks every node / fast checks every two nodes
        slow = head
        fast = head.next
        # shift slow and fast nodes unless both nodes meet toghter
        while slow != fast:
            # check if fast node reaches the end
            if not fast or not fast.next:
                return False
            # shift two nodes
            slow = slow.next
            fast = fast.next.next
        return True
        
```

# 3rd
レビューをもとに再度修正
- こちらに加えて、もう少し素直？な方法も実装してみると良いと思います。
（ノードを辿りながら以前に通ったノードかどうかを確認していく方法）

参照：https://mhiro216.hatenablog.com/entry/2019/08/17/103553

``` Python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # prepare checked nodes list as set 
        checked_nodes = set()
        # while head is not None check each node
        while head:
            if head in checked_nodes: # the second time to visit the head
                return True 
            else:                     # the first time to visit the head
                checked_nodes.add(head)
            head = head.next
        # if head is originally None or head reaches the end -> false (no cycle)
        return False 
```

# 4th
while文を少し書き直す．素直にfastとslowがNoneでない間はループを回して，重複があるときにTrueを返す，最後に到達してNoneになったらループを抜けてFalseを返す


以下のレビューが元です
- 個人的には重複があった（fast == slow）場合にループを切ってreturn Trueとする方が分かりやすいと感じました。

疑問
- どうしてもfast  = fast.next.nextでエラーにならないようにif not fast.nextをする必要があるのか？？？


``` Python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # check if head is null -> false (no cycle)
        if not head:
            return False
        # set pointer nodes, slow and fast
        # slow checks every node / fast checks every two nodes
        slow = head
        fast = head.next
        # shift slow and fast nodes unless both nodes meet toghter
        while fast and slow:
            if slow == fast:
                return True
            if not fast.next:
                return False
            slow = slow.next
            fast  = fast.next.next
        return False
```

# 5th
4thでの疑問を解消
- while fast and fast.nextとすればfast = fast.next.nextでエラーにならない


``` Python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # check if head is null -> false (no cycle)
        if not head:
            return False
        # set pointer nodes, slow and fast
        # slow checks every node / fast checks every two nodes
        slow = head
        fast = head.next
        # shift slow and fast nodes unless both nodes meet toghter
        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast  = fast.next.next
        return False
```