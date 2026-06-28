// TC : O(n)
// SC : O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Why to reverse the list because this is singly Linked List and we cannot walk backwards so we reverse the second half so that we attached the first head of the first part with second head of the second part and this second head will point to the first part next head there by doing the zigzag connection

        slow = head
        fast = head
        while fast.next and fast.next.next: # For getting the first middle node
            slow = slow.next
            fast = fast.next.next

        # Now we severe the connection 
        mid = slow.next
        slow.next = None


        # Now we reverse the second half
        prev = None
        curr = mid
        while (curr):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        

        headA = head
        headB = prev

        while (headB):
            temp1 = headA.next
            temp2 = headB.next
            headA.next = headB
            headB.next = temp1
            headA = temp1
            headB = temp2
