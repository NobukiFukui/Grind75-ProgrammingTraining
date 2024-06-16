# ===============================================================
# (program) 12_LinkedListCycle
# WaveAlchemist
# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached
#  again by continuously following the next pointer. Internally, pos is used to denote the index 
# of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
#
# URL: https://leetcode.com/problems/linked-list-cycle/description/
# ===============================================================

#%%
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
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

#%%
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
    