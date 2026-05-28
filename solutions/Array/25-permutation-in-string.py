//TC : O(n2)
//SC : O(1)
# This is relatively simple what if we could better

# from collections import Counter
# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         left = 0
#         k = len(s1)
#         seen = {}
#         target = Counter(s1)
#         for right in range(len(s2)):
#             seen[s2[right]] = seen.get(s2[right],0) + 1
#             if (right - left + 1) > k:
#                 seen[s2[left]] -= 1
#                 if seen[s2[left]] == 0:
#                     del seen[s2[left]]
#                 left += 1
            
#             if (right - left + 1) == k:
#                 if seen == target:
#                     return True
#         return False


# Different Approach
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        frequency_a = [0]*26
        frequency_b = [0]*26
        k = len(s1)
        n = len(s2)

        for char in s1:
            index = ord(char) - ord('a')
            frequency_a[index] += 1

        left = 0
        
        for right in range(n):
            index = ord(s2[right]) - ord('a')
            frequency_b[index] += 1

            if (right - left + 1) > k:
                left_index = ord(s2[left]) - ord('a')
                frequency_b[left_index] -= 1
                left += 1
            
            if(right - left + 1) == k:
                if frequency_a == frequency_b:
                    return True
        return False

