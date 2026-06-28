// TC : O(n)
// SC : O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if head == None:
        #     return head
        # p1 = head
        # p2 = p1.next

        # while (p2):
        #     while (p2 and p1.val == p2.val):
        #         p2 = p2.next
        #     p1.next = p2
        #     p1 = p2
        #     if (p1):
        #         p2 = p1.next
        # return head

        curr = head

        while curr and curr.next:

            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head