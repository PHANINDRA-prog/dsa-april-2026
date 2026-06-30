// TC : O(n)
// SC : O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Two Pass Approach

        # Find out the Tail
        # prev = None
        # curr = head
        # while curr:
        #     nxt = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = nxt
        
        # temp = prev
        # just_prev = temp
        # if (n == 1):
        #     t = prev.next
        #     prev.next = None
        #     prev = t
        #     head = prev
        #     prev = None
        #     curr = head
        #     while curr:
        #         nxt = curr.next
        #         curr.next = prev
        #         prev = curr
        #         curr = nxt
        #     return prev

        # while n > 1 and temp.next:
        #     just_prev = temp
        #     temp = temp.next
        #     n -= 1
        
        # just_prev.next = temp.next
        
        # head = prev

        # prev = None
        # curr = head
        # while curr:
        #     nxt = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = nxt
        # return prev


        dummy = ListNode(0)
        dummy.next = head

        slow = dummy
        fast = dummy

        for _ in range(n+1):
            fast = fast.next
        
        while fast:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        return dummy.next