// TC : O(n)
// SC : O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Brute Force Solution
        # arr = []
        # curr = head
        # while (curr):
        #     arr.append(curr.val)
        #     curr = curr.next
        
        # return arr == arr[::-1]

        # My solution Optimzed One
        # if head.next == None:
        #     return True

        # slow = head
        # fast = head
        # prev = None
        # while fast and fast.next:
        #     prev = slow
        #     slow = slow.next
        #     fast = fast.next.next
        
        # isEven = False
        # isOdd = False

        # if (prev.val == slow.val):
        #     isEven = True
        
        # if (slow.next and (prev.val == slow.next.val)):
        #     isOdd = True
        
        # if (isEven == False and isOdd == False):
        #     return False
        
        
        # if (isEven):
        #     prev.next = None

        #     rev_prev = None
        #     curr = slow
        #     while (curr):
        #         nxt = curr.next
        #         curr.next = rev_prev
        #         rev_prev = curr
        #         curr = nxt
            
        #     new_head = rev_prev
        #     temp1= new_head
        #     temp = head

        #     while (temp):
        #         if(temp.val == temp1.val):
        #             temp = temp.next
        #             temp1 = temp1.next
        #         else:
        #             return False
        #     return True
        
        # if (isOdd):
        #     prev.next = None

        #     rev_prev = None
        #     curr = slow.next
        #     while (curr):
        #         nxt = curr.next
        #         curr.next = rev_prev
        #         rev_prev = curr
        #         curr = nxt
            
        #     new_head = rev_prev
        #     temp1 = new_head
        #     temp = head
        #     while (temp):
        #         if(temp and temp1 and temp.val == temp1.val):
        #             temp = temp.next
        #             temp1 = temp1.next
        #         else:
        #             return False
        #     return True      

        slow = head
        fast = head

        # Find the Middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # The Most Important for Odd and Even if for odd length fast will not be None and for even length fast is None

        if fast:
            slow = slow.next

        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        left = head
        right = prev
        
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True