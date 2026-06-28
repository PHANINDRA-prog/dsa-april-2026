// TC : O(n)
// SC : O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Brute Force Approach with extra space
        # # hashmap = {}
        # hashset = set()
        # curr = head
        # while curr:
        #     if curr in hashset:
        #         return True
        #     # hashmap[curr] = hashmap.get(curr,0) + 1
        #     hashset.add(curr)
        #     curr = curr.next
        # return False


        # Now Optimized Fast and Slow Pointers
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if (slow == fast):
                return True
        return False            