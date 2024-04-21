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