// TC : O(n)
// SC : O(1)
# Brute Force Approach
        # # hashmap = {}
        # hashset = set()
        # curr = head
        # while curr:
        #     if curr in hashset:
        #         return curr
        #     # hashmap[curr] = hashmap.get(curr,0) + 1
        #     hashset.add(curr)
        #     curr = curr.next
        # return None

        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if (slow == fast):
                fast = head
                while (fast != slow):
                    fast = fast.next
                    slow = slow.next
                return slow
        return None           